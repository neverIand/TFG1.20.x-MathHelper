from typing import Dict, List, Tuple


def find_compositions(materials: Dict[str, Tuple[int, int]], unit_volume: int, max_volume: int) -> List[Dict[str, int]]:
    """
    Finds valid compositions based on the provided material percentage ranges, unit volume, and maximum volume.

    Args:
    - materials: A dictionary where keys are material names and values are tuples of (min_percentage, max_percentage).
    - unit_volume: The volume of one unit of any material in mb.
    - max_volume: The maximum total volume of the composition in mb.

    Returns:
    A list of dictionaries, where each dictionary represents a valid composition with material names as keys and
    the number of units as values.
    """
    from itertools import product

    # Initialize variables
    valid_compositions = []
    material_names = list(materials.keys())
    ranges = [range(int(max_volume * materials[material][0] / 100 / unit_volume),
                    int(max_volume * materials[material][1] / 100 / unit_volume) + 1) for material in material_names]

    # Generate all possible combinations of units for each material within their specified ranges
    for units in product(*ranges):
        total_volume = sum(units) * unit_volume
        if total_volume > max_volume:
            continue  # Skip compositions that exceed the maximum volume

        composition = dict(zip(material_names, units))
        percentages = {material: (units[i] * unit_volume) / total_volume * 100 for i, material in
                       enumerate(material_names)}

        # Check if the composition fits within the specified percentage ranges for all materials
        if all(materials[material][0] <= percentages[material] <= materials[material][1] for material in materials):
            valid_compositions.append(composition)

    return valid_compositions


# Example usage with a more generic set of materials
materials_example = {
    'steel': (20, 25),
    'rose_gold': (10, 15),
    'black_steel': (50, 55),
    'brass': (10, 15)
}

# Find valid compositions for the example materials
valid_compositions_example = find_compositions(materials_example, 144, 4000)
print(valid_compositions_example)
