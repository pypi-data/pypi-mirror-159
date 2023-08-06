import re
from collections import ChainMap
from typing import Any
from typing import Dict

from idem_codegen.idem_codegen.tool.utils import (
    separator,
)

attributes_to_ignore = ["resource_id", "name", "tags", "arn"]


def arg_bind(hub, sls_data: Dict[str, Any], idem_resource_id_map) -> Dict[str, Any]:
    arg_binded_sls_data = hub.idem_codegen.generator.argument_binder.default.arg_bind(
        sls_data, idem_resource_id_map
    )

    # Special arg binding logic for ternary operator
    ternary_operator_pattern = re.compile(
        r"\${[\s\d\w. ]+\?[\s\d\w.[\] ]+:[\s\d\w.[\] ]+}|[\s\d\w. ]+\?[\s\d\w.[\] ]+:[\s\d\w.[\] ]+"
    )
    var_pattern = re.compile(r"var\.[\w-]+")
    terraform_resource_map = hub.tf_idem.RUNS["TF_RESOURCE_MAP"]

    if not terraform_resource_map:
        hub.log.warning(
            "Not able to handle arg binding in ternary operator, Terraform resource map is not found in hub."
        )
        return arg_binded_sls_data

    for item in arg_binded_sls_data:
        resource_attributes = list(sls_data[item].values())[0]
        resource_type = list(sls_data[item].keys())[0].replace(".present", "")
        resource_map = dict(ChainMap(*resource_attributes))

        # get terraform resource to look for ternary operator
        terraform_resource = terraform_resource_map.get(
            f"{resource_type}{separator}{resource_map.get('resource_id')}"
        )

        for resource_attribute in resource_attributes:
            for (
                resource_attribute_key,
                resource_attribute_value,
            ) in resource_attribute.items():

                if (
                    terraform_resource
                    and resource_attribute_key not in attributes_to_ignore
                ):
                    (
                        tf_resource_value,
                        tf_resource_key,
                        is_attribute_different,
                    ) = hub.tf_idem.tool.utils.get_tf_equivalent_idem_attribute(
                        terraform_resource,
                        list(terraform_resource.keys())[0],
                        resource_attribute_key,
                    )
                    if isinstance(
                        tf_resource_value, str
                    ) and ternary_operator_pattern.search(tf_resource_value):
                        if tf_resource_value.startswith("${"):
                            tf_resource_value = tf_resource_value[2:-1]
                        expression = tf_resource_value.split("?")[0].strip()
                        true_block = (
                            tf_resource_value.split("?")[1].split(":")[0].strip()
                        )
                        false_block = (
                            tf_resource_value.split("?")[1].split(":")[1].strip()
                        )
                        if not re.match(var_pattern, expression):
                            expression = convert_string_into_arg_bind_format(
                                hub, expression
                            )
                        if not re.match(var_pattern, true_block):
                            true_block = convert_string_into_arg_bind_format(
                                hub, true_block
                            )
                        if not re.match(var_pattern, false_block):
                            false_block = convert_string_into_arg_bind_format(
                                hub, false_block
                            )
                        resource_attribute[
                            resource_attribute_key
                        ] = f"{expression} ? {true_block} : {false_block}"
    return arg_binded_sls_data


def convert_string_into_arg_bind_format(hub, value: str):
    if value.startswith("data."):
        return value
    else:
        tf_resource_type = value[: value.find(".")]
        tf_resource_attribute = value[value.rfind(".") + 1 :]
        resource_state_name = value[value.find(".") + 1 : value.rfind(".")]

        # if resource_state_name is of type 'cluster', then no need to convert
        # if resource_state_name is of type 'cluster[0]', then convert it to 'cluster-0'
        # if resource_state_name is of type 'cluster[count.index]', then convert it to 'cluster-{{i}}'
        # if resource_state_name is of type 'cluster[xyz]', then convert it to 'cluster-{{xyz}}'
        if resource_state_name.endswith("]"):
            var_name = resource_state_name[: resource_state_name.find("[")]
            index = resource_state_name[resource_state_name.find("[") + 1 : -1]
            if index.isdigit():
                resource_state_name = f"{var_name}-{index}"
            elif index == "count.index":
                resource_state_name = var_name + "-{{i}}"
            else:
                resource_state_name = var_name + "-{{" + index + "}}"

        if tf_resource_attribute.strip() == "id":
            tf_resource_attribute = "resource_id"
        elif tf_resource_type in hub.tf_idem.tool.utils.tf_equivalent_idem_attributes:
            idem_equivalent_tf_resource_attributes = (
                hub.tf_idem.tool.utils.tf_equivalent_idem_attributes[tf_resource_type]
            )
            if tf_resource_attribute in list(
                idem_equivalent_tf_resource_attributes.values()
            ):
                for key, value in idem_equivalent_tf_resource_attributes:
                    if value == tf_resource_attribute:
                        tf_resource_attribute = key

        return (
            "${"
            + f"{hub.tf_idem.tool.utils.tf_idem_resource_type_map.get(tf_resource_type)}:{tf_resource_type}.{resource_state_name}:{tf_resource_attribute}"
            + "}"
        )
