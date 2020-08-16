"""Create new worlds for gazebo."""

import argparse
import copy
import xml.etree.ElementTree as et

GROUND_X = 13.9805
GROUND_Y = 20.9067
names_to_remove = [
    "aws_robomaker_warehouse_WallB_01_001",
    "aws_robomaker_warehouse_ClutteringA_01_016",
    "aws_robomaker_warehouse_ClutteringA_01_017",
    "aws_robomaker_warehouse_ClutteringC_01_032",
    "aws_robomaker_warehouse_Bucket_01_020",
    "aws_robomaker_warehouse_Bucket_01_022",
    "aws_robomaker_warehouse_PalletJackB_01_001",
]


def create_no_roof_no_walls_small_warehouse_9():
    tree = et.parse("no_roof_small_warehouse.world")
    root = tree.getroot()
    root_copy = copy.deepcopy(root)

    xml_header = "<?xml version='1.0' encoding='utf-8'?>"

    for element in root.iter():
        if element.tag in ["model", "light"]:
            if (
                element.tag not in ["gravity", "physics", "gui"]
                and element.attrib["name"] not in names_to_remove
            ):
                for x_count, x_val in enumerate([0, GROUND_X, -GROUND_X]):
                    for y_count, y_val in enumerate([0, GROUND_Y, -GROUND_Y]):
                        if x_count + y_count != 0:
                            new_model = copy.deepcopy(element)
                            new_model.set("name", f"{new_model.attrib['name']}_{x_count}_{y_count}")
                            new_model_pose = new_model.find("pose").text.split(" ")
                            new_model_pose[0] = str(float(new_model_pose[0]) + x_val)
                            new_model_pose[1] = str(float(new_model_pose[1]) + y_val)
                            new_model.find("pose").text = " ".join(new_model_pose)
                            root_copy.find("world").append(new_model)

    for name in names_to_remove:
        item = root_copy.find(f".//*[@name='{name}']")
        root_copy.find("world").remove(item)

    xml = xml_header + et.tostring(root_copy).decode("utf-8")

    with open("no_roof_no_walls_small_warehouse_9.world", "w") as out:
        out.write(xml)


def create_no_roof_no_walls_small_warehouse_25():
    tree = et.parse("no_roof_small_warehouse.world")
    root = tree.getroot()
    root_copy = copy.deepcopy(root)

    xml_header = "<?xml version='1.0' encoding='utf-8'?>"

    for element in root.iter():
        if element.tag in ["model", "light"]:
            if (
                element.tag not in ["gravity", "physics", "gui"]
                and element.attrib["name"] not in names_to_remove
            ):
                for x_count, x_val in enumerate(
                    [0, GROUND_X, -GROUND_X, 2 * GROUND_X, -2 * GROUND_X]
                ):
                    for y_count, y_val in enumerate(
                        [0, GROUND_Y, -GROUND_Y, 2 * GROUND_Y, -2 * GROUND_Y]
                    ):
                        if x_count + y_count != 0:
                            new_model = copy.deepcopy(element)
                            new_model.set("name", f"{new_model.attrib['name']}_{x_count}_{y_count}")
                            new_model_pose = new_model.find("pose").text.split(" ")
                            new_model_pose[0] = str(float(new_model_pose[0]) + x_val)
                            new_model_pose[1] = str(float(new_model_pose[1]) + y_val)
                            new_model.find("pose").text = " ".join(new_model_pose)
                            root_copy.find("world").append(new_model)

    for name in names_to_remove:
        item = root_copy.find(f".//*[@name='{name}']")
        root_copy.find("world").remove(item)

    xml = xml_header + et.tostring(root_copy).decode("utf-8")

    with open("no_roof_no_walls_small_warehouse_25.world", "w") as out:
        out.write(xml)


def create_no_roof_no_walls_small_warehouse_9_only_racks():
    tree = et.parse("no_roof_small_warehouse.world")
    root = tree.getroot()
    root_copy = copy.deepcopy(root)
    names_to_remove_local = copy.deepcopy(names_to_remove)

    xml_header = "<?xml version='1.0' encoding='utf-8'?>"

    for element in root.iter():
        if element.tag in ["model", "light"]:
            if element.tag not in ["gravity", "physics", "gui"] and element.attrib["name"] in [
                "aws_robomaker_warehouse_ShelfF_01_001",
                "Warehouse_CeilingLight_003",
                "aws_robomaker_warehouse_GroundB_01_001",
                "aws_robomaker_warehouse_Lamp_01_005",
            ]:
                for x_count, x_val in enumerate([0, GROUND_X, -GROUND_X]):
                    for y_count, y_val in enumerate([0, GROUND_Y, -GROUND_Y]):
                        if x_count + y_count != 0:
                            new_model = copy.deepcopy(element)
                            new_model.set("name", f"{new_model.attrib['name']}_{x_count}_{y_count}")
                            new_model_pose = new_model.find("pose").text.split(" ")
                            new_model_pose[0] = str(float(new_model_pose[0]) + x_val)
                            new_model_pose[1] = str(float(new_model_pose[1]) + y_val)
                            new_model.find("pose").text = " ".join(new_model_pose)
                            root_copy.find("world").append(new_model)
            else:
                names_to_remove_local.append(element.attrib["name"])

    for name in names_to_remove_local:
        items = root_copy.findall(f".//*[@name='{name}']")
        for item in items:
            root_copy.find("world").remove(item)

    xml = xml_header + et.tostring(root_copy).decode("utf-8")

    with open("no_roof_no_walls_small_warehouse_9_only_racks.world", "w") as out:
        out.write(xml)

def create_no_roof_no_walls_small_warehouse_25_only_racks():
    tree = et.parse("no_roof_small_warehouse.world")
    root = tree.getroot()
    root_copy = copy.deepcopy(root)
    names_to_remove_local = copy.deepcopy(names_to_remove)

    xml_header = "<?xml version='1.0' encoding='utf-8'?>"

    for element in root.iter():
        if element.tag in ["model", "light"]:
            if element.tag not in ["gravity", "physics", "gui"] and element.attrib["name"] in [
                "aws_robomaker_warehouse_ShelfF_01_001",
                "Warehouse_CeilingLight_003",
                "aws_robomaker_warehouse_GroundB_01_001",
                "aws_robomaker_warehouse_Lamp_01_005",
            ]:
                for x_count, x_val in enumerate(
                    [0, GROUND_X, -GROUND_X, 2 * GROUND_X, -2 * GROUND_X]
                ):
                    for y_count, y_val in enumerate(
                        [0, GROUND_Y, -GROUND_Y, 2 * GROUND_Y, -2 * GROUND_Y]
                    ):
                        if x_count + y_count != 0:
                            new_model = copy.deepcopy(element)
                            new_model.set("name", f"{new_model.attrib['name']}_{x_count}_{y_count}")
                            new_model_pose = new_model.find("pose").text.split(" ")
                            new_model_pose[0] = str(float(new_model_pose[0]) + x_val)
                            new_model_pose[1] = str(float(new_model_pose[1]) + y_val)
                            new_model.find("pose").text = " ".join(new_model_pose)
                            root_copy.find("world").append(new_model)
            else:
                names_to_remove_local.append(element.attrib["name"])

    for name in names_to_remove_local:
        items = root_copy.findall(f".//*[@name='{name}']")
        for item in items:
            root_copy.find("world").remove(item)

    xml = xml_header + et.tostring(root_copy).decode("utf-8")

    with open("no_roof_no_walls_small_warehouse_25_only_racks.world", "w") as out:
        out.write(xml)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--world-name", help="Set world name.", action="store", required=True, type=str
    )

    # Example:
    # python create_world.py --world-name 'no_roof_no_walls_small_warehouse_9'
    args = parser.parse_args()

    if args.world_name == "no_roof_no_walls_small_warehouse_9":
        create_no_roof_no_walls_small_warehouse_9()
    elif args.world_name == "no_roof_no_walls_small_warehouse_25":
        create_no_roof_no_walls_small_warehouse_25()
    elif args.world_name == "no_roof_no_walls_small_warehouse_9_only_racks":
        create_no_roof_no_walls_small_warehouse_9_only_racks()
    elif args.world_name == "no_roof_no_walls_small_warehouse_25_only_racks":
        create_no_roof_no_walls_small_warehouse_25_only_racks()
