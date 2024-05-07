import math

import pytest
from processing.transformations import identify_unit, convert_unit, extract_unit_name, extract_quantity, \
    identify_item_count

test_data = [
    ('48 g (2 PIECES)', 'mass', 48.000, 'g (2 PIECES)', 2.0),
    ('57 g (1 PACKAGE)', 'mass', 57.000, 'g (1 PACKAGE)', 1.0),
    ('6 g (1 tsp)', 'mass', 6.000, 'g (1 tsp)',  1.0),
    ('355 ml (1 CAN)', 'volume', 0.355, 'ml (1 CAN)',  1.0),
    ('20 g', 'mass', 20.000, 'g',  None),
    ('170 g (6 oz)', 'mass', 170.00, 'g (6 oz)',  None),
    ('130 g (6 | APPROX)', 'mass', 130.000, 'g (6 | APPROX)',  6.0),
    ('132 g (0.3333 PIZZA)', 'mass', 132.000, 'g (0.3333 PIZZA)',  0.3333),
    ('21 g (1 Tbsp)', 'mass', 21.000, 'g (1 Tbsp)',  1.0),
    ('57 g (57 g)', 'mass', 57.000, 'g (57 g)',  None),
    ('85 g (3 CUPS | ABOUT)', 'mass', 85.000, 'g (3 CUPS | ABOUT)',  3),
    ('28 g (18 CHIPS) | (ABOUT)', 'mass', 28.000, 'g (18 CHIPS) | (ABOUT)',  18),
    ('2 ml (0.041 BOTTLE)', 'volume', 0.002, 'ml (0.041 BOTTLE)',  0.041),
    ('45 g (0.25 cup)', 'mass', 45.000, 'g (0.25 cup)',  0.25),
    ('28 g (1 ONZ)', 'mass', 28.000, 'g (1 ONZ)',  1),
    ('1.2 g (0.25 tsp)', 'mass', 1.200, 'g (0.25 tsp)', '1.2', 0.25),
    ('39 g (1 BUN)', 'mass', 39.000, 'g (1 BUN)',  1),
    ('140 g', 'mass', 140.000, 'g',  None),
    ('56 g (2 oz)', 'mass', 56.00, 'g (2 oz)',  None),
    ('20 g (1 SLICES)', 'mass', 20.000, 'g (1 SLICES)',  1),
    ('100g', 'mass', 100.000, 'g',  None),
    ('99 g (0.5 cup)', 'mass', 99.000, 'g (0.5 cup)',  0.5),
    ('113 g (1 BURGER)', 'mass', 113.000, 'g (1 BURGER)',  1),
    ('3 bâtonnets 100g', 'mass', None, "bâtonnets 100g",  None),
    ('30 g (1 oz)', 'mass', 30.00, 'g (1 oz)',  None),
    ('400 g', 'mass', 400.000, 'g',  None),
    ('31 g (1 cup)', 'mass', 31.000, 'g (1 cup)',  1),
    ('250 ml', 'volume', 0.250, 'ml',  None)
]

TOLERANCE = 1e-6

# Create a pytest parameterized test
@pytest.mark.parametrize("input_value, expected_type, expected_value, expected_uni, expected_items", test_data)
def test_serving_size_processing(input_value, expected_type, expected_value, expected_unit, expected_quantity, expected_items):
    assert identify_unit(input_value) == expected_type

    assert convert_unit(input_value, expected_type) == pytest.approx(expected_value, rel=TOLERANCE)

    assert extract_unit_name(input_value) == expected_unit

    item_count = identify_item_count(input_value)
    assert item_count == expected_items if expected_items is not None else math.isnan(item_count)
