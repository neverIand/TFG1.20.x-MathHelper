# [TFG1.20.x](https://github.com/TerraFirmaGreg-Team/Modpack-1.20.x)-MathHelper
***
## Table of Content

- [`AlloyForge.py`](#alloyforgepy)
- [`AlloyRecipeFinder.py`](#alloyrecipefinderpy)
- [`FurnaceCalculator.py`](#furnacecalculatorpy)

## AlloyForge.py
Replace operations in `test_final_operations` with the order you need and it will try to find the minimum operations needed. Known issue: it will terminate the search directly is the final operations added to a negative value.  

## AlloyRecipeFinder.py
Print out 5 possible combinations of material given the type of metal and the ratio.

## FurnaceCalculator.py
Calculate the most cost-efficient way of smelting the given metal ore in the furnace.

***

## TODO
- Cleanup
- Fix known issues in `AlloyForge.py`
- Improve documentation
- EN variables/operations in scripts