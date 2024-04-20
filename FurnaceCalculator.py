def calculate_efficient_smelting_with_minimum_threshold(ore_mb: int, min_threshold: int = 18) -> tuple:
    """
    计算单种金属熔炼的最优数量和浪费量，确保熔炼效率最高，同时考虑最小熔炼量的要求。

    :param ore_mb: 单块矿石的mb数
    :param min_threshold: 接受的最小熔炼矿石数量，如果最优解小于此值，会尝试寻找产量更高的解决方案
    :return: (最佳矿石数量, 对应的浪费mb数, 熔炼出的金属总mb数)
    """
    max_ore_count = 24  # 炉子中最多可以容纳的矿石数量
    closest_to_full_use = 0  # 最接近144mb整数倍的矿石使用量
    minimal_waste = float('inf')  # 初始化最小浪费量为无穷大
    optimal_ore_count = 0  # 最优的矿石数量

    for n in range(1, max_ore_count + 1):
        total_ore_mb = n * ore_mb  # 当前数量矿石的总mb数
        full_bars_possible = total_ore_mb // 144  # 完整金属锭的数量
        waste_mb = total_ore_mb - (full_bars_possible * 144)  # 当前浪费量

        # 如果当前组合浪费更少，更新最优解
        if waste_mb < minimal_waste or (waste_mb == minimal_waste and total_ore_mb > closest_to_full_use):
            minimal_waste = waste_mb
            optimal_ore_count = n
            closest_to_full_use = total_ore_mb

    # 如果找到的最佳矿石数量小于最小阈值，尝试寻找产量更高但浪费稍多的方案
    if optimal_ore_count < min_threshold:
        for n in range(min_threshold, max_ore_count + 1):
            total_ore_mb = n * ore_mb
            full_bars_possible = total_ore_mb // 144
            waste_mb = total_ore_mb - (full_bars_possible * 144)

            # 更新条件：接受更多的浪费以提高总产量
            if total_ore_mb > closest_to_full_use and waste_mb <= ore_mb:  # 允许的浪费不超过一个矿石的mb
                optimal_ore_count = n
                minimal_waste = waste_mb
                closest_to_full_use = total_ore_mb

    optimal_total_mb = optimal_ore_count * ore_mb
    full_bars = optimal_total_mb // 144
    optimal_waste = optimal_total_mb - (full_bars * 144)

    return optimal_ore_count, optimal_waste, optimal_total_mb


# 示例
# test_ore_mb = 121
test_ore_mb = 129

test_result = calculate_efficient_smelting_with_minimum_threshold(test_ore_mb)

print(f"矿石: 每种矿石容量 = {test_ore_mb}mb, 最佳数量 = {test_result[0]}, 浪费 = {test_result[1]}mb, 总量 = {test_result[2]}mb")
