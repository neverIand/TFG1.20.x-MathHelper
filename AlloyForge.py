def forge_tool_optimized_with_pruning_and_memoization(target, operations, sequence, best_sequence, max_operations, memo,
                                                      depth=0):
    current_value = sum(operations[op] for op in sequence)
    sequence_key = tuple(sequence)

    # 使用剪枝和缓存结果
    if sequence_key in memo:
        return memo[sequence_key]
    if current_value == target:
        memo[sequence_key] = sequence
        return sequence if not best_sequence or len(sequence) < len(best_sequence) else best_sequence
    if current_value > target or len(sequence) >= max_operations:
        return best_sequence

    for op in operations:
        new_sequence = sequence + [op]
        candidate_sequence = forge_tool_optimized_with_pruning_and_memoization(target, operations, new_sequence,
                                                                               best_sequence, max_operations, memo,
                                                                               depth + 1)
        if candidate_sequence and (not best_sequence or len(candidate_sequence) < len(best_sequence)):
            best_sequence = candidate_sequence

    memo[sequence_key] = best_sequence
    return best_sequence


# Function to find the best forging sequence for any given final three operations with optimizations
def find_best_forging_sequence_optimized(operations, final_operations, max_operations=10):
    memo = {}
    best_sequence = forge_tool_optimized_with_pruning_and_memoization(-sum(operations[op] for op in final_operations),
                                                                      operations, [], None, max_operations, memo)
    return best_sequence + final_operations if best_sequence else None


def find_best_forging_sequence_for_different_target(operations, final_operations, target_end_value, max_operations=10):
    # 计算最后三个操作前需要达到的目标值
    target_start_value = target_end_value - sum(operations[op] for op in final_operations)
    print(target_start_value)
    memo = {}
    best_sequence = forge_tool_optimized_with_pruning_and_memoization(target_start_value, operations, [], None,
                                                                      max_operations, memo)
    return best_sequence + final_operations if best_sequence else None


operations = {
    "轻击": -3,
    "击打": -6,
    "重击": -9,
    "牵拉": -15,
    "冲压": +2,
    "弯曲": +7,
    "镦锻": +13,
    "收缩": +16
}

# 最后三个操作
# test_final_operations = ["弯曲", "弯曲"] # 鼓风口
# test_final_operations = ["牵拉", "弯曲", "击打"]
# test_final_operations = ["弯曲", "冲压", "镦锻"]
# 黄铜： ['镦锻', '收缩'*5, '击打', '击打', '击打']

# 锻铁锭 stage1: ['冲压', '收缩'*6, '击打', '击打', '击打']; stage2: ['弯曲'* 3, '收缩'*4, '击打', '击打', '击打']
# 锻铁板： ['冲压', '镦锻', '镦锻', '收缩'*4， '击打', '击打', '击打']

# 锻铁灯：['冲压', '镦锻', '镦锻', '收缩', '收缩', '收缩', '收缩', '牵拉', '弯曲', '弯曲']

# 高碳钢： ['冲压', '镦锻', '镦锻', '收缩'*6, '击打', '击打', '击打']
# 钢： ['冲压', '弯曲', '收缩'*6, '击打', '击打', '击打']
# 钢板：['弯曲'*2, '镦锻'*2, '收缩'*3, '击打', '击打', '击打']

# 钢镐： ['弯曲', '弯曲', '镦锻', '镦锻', '收缩', '收缩', '收缩', '收缩', '弯曲', '牵拉','冲压']

# 钢斧：['弯曲', '弯曲', '弯曲', '收缩', '收缩', '收缩', '收缩', '收缩', '镦锻', '击打', '冲压']

# 钢锻造锤：['弯曲', '收缩', '收缩', '冲压']

# 钢鼓风口： ['冲压', '镦锻', '镦锻', '收缩', '弯曲', '弯曲']

# Unfinished iron flask ['冲压', '弯曲', '镦锻', '收缩', '弯曲', '弯曲', '冲压']

# 黄铜板： ['镦锻', '收缩'*4, '击打', '击打', '击打']

# 黄铜机件：['弯曲', '镦锻'*2, '收缩'*4, '冲压', '击打', '冲压']

# 黄铜file head: ['冲压', '弯曲', '收缩', '收缩', '弯曲', '冲压', '镦锻']

# 黄铜杆： ['弯曲', '弯曲', '镦锻', '收缩'*5, '牵拉', '牵拉', '弯曲']

# 铜龙头：['弯曲', '镦锻', '镦锻', '收缩', '收缩', '收缩', '收缩', '牵拉', '击打', '收缩']

# 未完成 钢胸甲 ['镦锻', '收缩', '收缩', '收缩', '收缩', '镦锻', '击打', '击打']
# 未完成 钢头盔 ['冲压', '镦锻', '镦锻', '收缩', '弯曲', '弯曲', '击打']
# 未完成 钢护腿 (配平后) ['弯曲', '弯曲','弯曲', '牵拉', '击打']
# 未完成 钢靴子 ['冲压', '弯曲', '镦锻', '收缩', '弯曲', '弯曲']

# 钢 knife head ['弯曲', '镦锻', '收缩'*5, '牵拉', '弯曲', '冲压']

# 目标值
test_final_operations = ["牵拉", "弯曲", "击打"]
target_end_value_test = 0
best_sequence_for_different_target = find_best_forging_sequence_for_different_target(operations, test_final_operations,
                                                                                     target_end_value_test,
                                                                                     max_operations=8)
print(best_sequence_for_different_target)
