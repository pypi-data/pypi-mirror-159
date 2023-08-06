"""Contains logic to compare gpus"""


def compare_gpus(gpu_spec_list: list[dict[str, str]]) -> str:
    """Compare GPU specs

    Args:
        gpu_spec_list (list[dict[str, str]]): a list of dictionaries having gpu specs

    Returns:
        str: dictionary as string containing performance comparison of GPUs

    Examples:
        .. code:: python

            >>> compare_gpus([{'gpu_name': 'A2', 'architecture': 'ampere', 'int8_perf': '36', 'mem_bandwidth': '200'}, {'gpu_name': 'A10', 'architecture': 'ampere', 'int8_perf': '250', 'mem_bandwidth': '600'}, {'gpu_name': 'A30', 'architecture': 'ampere', 'int8_perf': '330', 'mem_bandwidth': '933'}])
            "{'A10/A2': '3.0x', 'A30/A2': '4.67x'}"
    """
    # params to compare
    spec_params = ["mem_bandwidth", "cuda_cores", "fp32_perf", "int8_perf", "fp16_perf"]
    # store spec comparison of gpus
    gpu_spec_comparison = {}
    # take first gpu as base gpu to compare with
    base_gpu_spec = gpu_spec_list[0]
    # compare rest gpus with base gpu
    for gpu_spec in gpu_spec_list[1:]:
        # difference in gpu performance
        gpu_perf_diff = float("inf")
        # iterate the specs which are to be compared
        for spec in spec_params:
            # check if spec data exists
            if spec in gpu_spec:
                perf_ratio = float(gpu_spec[spec]) / float(base_gpu_spec[spec])
                # take min criterion
                if perf_ratio < gpu_perf_diff:
                    gpu_perf_diff = perf_ratio
        gpu_spec_comparison[gpu_spec["gpu_name"] + "/" + base_gpu_spec["gpu_name"]] = (
            str(round(gpu_perf_diff, 2)) + "x"
        )

    return f"{gpu_spec_comparison}"
