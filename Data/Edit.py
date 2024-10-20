import os
import shutil

# Paths to the dataset and labels
data_dir = 'data'  # Where your images are stored
train_txt = 'train.txt'
test_txt = 'test.txt'

# Mapping of class labels to bird species names
label_to_bird = {
    0: 'Black_footed_Albatross',
    1: 'Laysan_Albatross',
    2: 'Sooty_Albatross',
    3: 'Groove_billed_Ani',
    4: 'Crested_Auklet',
    5: 'Least_Auklet',
    6: 'Parakeet_Auklet',
    7: 'Rhinoceros_Auklet',
    8: 'Brewer_Blackbird',
    9: 'Red_winged_Blackbird',
    10: 'Rusty_Blackbird',
    11: 'Yellow_headed_Blackbird',
    12: 'Bobolink',
    13: 'Indigo_Bunting',
    14: 'Lazuli_Bunting',
    15: 'Painted_Bunting',
    16: 'Cardinal',
    17: 'Spotted_Catbird',
    18: 'Gray_Catbird',
    19: 'Yellow_breasted_Chat',
    20: 'Eastern_Towhee',
    21: 'Chuck_will_Widow',
    22: 'Brandt_Cormorant',
    23: 'Red_faced_Cormorant',
    24: 'Pelagic_Cormorant',
    25: 'Bronzed_Cowbird',
    26: 'Shiny_Cowbird',
    27: 'Brown_Creeper',
    28: 'American_Crow',
    29: 'Fish_Crow',
    30: 'Black_billed_Cuckoo',
    31: 'Mangrove_Cuckoo',
    32: 'Yellow_billed_Cuckoo',
    33: 'Gray_crowned_Rosy_Finch',
    34: 'Purple_Finch',
    35: 'Northern_Flicker',
    36: 'Acadian_Flycatcher',
    37: 'Great_Crested_Flycatcher',
    38: 'Least_Flycatcher',
    39: 'Olive_sided_Flycatcher',
    40: 'Scissor_tailed_Flycatcher',
    41: 'Vermilion_Flycatcher',
    42: 'Yellow_bellied_Flycatcher',
    43: 'Frigatebird',
    44: 'Northern_Fulmar',
    45: 'Gadwall',
    46: 'American_Goldfinch',
    47: 'European_Goldfinch',
    48: 'Boat_tailed_Grackle',
    49: 'Eared_Grebe',
    50: 'Horned_Grebe',
    51: 'Pied_billed_Grebe',
    52: 'Western_Grebe',
    53: 'Blue_Grosbeak',
    54: 'Evening_Grosbeak',
    55: 'Pine_Grosbeak',
    56: 'Rose_breasted_Grosbeak',
    57: 'Pigeon_Guillemot',
    58: 'California_Gull',
    59: 'Glaucous_winged_Gull',
    60: 'Heermann_Gull',
    61: 'Herring_Gull',
    62: 'Ivory_Gull',
    63: 'Ring_billed_Gull',
    64: 'Slaty_backed_Gull',
    65: 'Western_Gull',
    66: 'Anna_Hummingbird',
    67: 'Ruby_throated_Hummingbird',
    68: 'Rufous_Hummingbird',
    69: 'Green_Violetear',
    70: 'Long_tailed_Jaeger',
    71: 'Pomarine_Jaeger',
    72: 'Blue_Jay',
    73: 'Florida_Jay',
    74: 'Green_Jay',
    75: 'Dark_eyed_Junco',
    76: 'Tropical_Kingbird',
    77: 'Gray_Kingbird',
    78: 'Belted_Kingfisher',
    79: 'Green_Kingfisher',
    80: 'Pied_Kingfisher',
    81: 'Ringed_Kingfisher',
    82: 'White_breasted_Kingfisher',
    83: 'Red_legged_Kittiwake',
    84: 'Horned_Lark',
    85: 'Pacific_Loon',
    86: 'Mallard',
    87: 'Western_Meadowlark',
    88: 'Hooded_Merganser',
    89: 'Red_breasted_Merganser',
    90: 'Mockingbird',
    91: 'Nighthawk',
    92: 'Clark_Nutcracker',
    93: 'White_breasted_Nuthatch',
    94: 'Baltimore_Oriole',
    95: 'Hooded_Oriole',
    96: 'Orchard_Oriole',
    97: 'Scott_Oriole',
    98: 'Ovenbird',
    99: 'Brown_Pelican',
    100: 'White_Pelican',
    101: 'Western_Wood_Pewee',
    102: 'Sayornis',
    103: 'American_Pipit',
    104: 'Whip_poor_Will',
    105: 'Horned_Puffin',
    106: 'Common_Raven',
    107: 'White_necked_Raven',
    108: 'American_Redstart',
    109: 'Geococcyx',
    110: 'Loggerhead_Shrike',
    111: 'Great_Grey_Shrike',
    112: 'Baird_Sparrow',
    113: 'Black_throated_Sparrow',
    114: 'Brewer_Sparrow',
    115: 'Chipping_Sparrow',
    116: 'Clay_colored_Sparrow',
    117: 'House_Sparrow',
    118: 'Field_Sparrow',
    119: 'Fox_Sparrow',
    120: 'Grasshopper_Sparrow',
    121: 'Harris_Sparrow',
    122: 'Henslow_Sparrow',
    123: 'Le_Conte_Sparrow',
    124: 'Lincoln_Sparrow',
    125: 'Nelson_Sharp_tailed_Sparrow',
    126: 'Savannah_Sparrow',
    127: 'Seaside_Sparrow',
    128: 'Song_Sparrow',
    129: 'Tree_Sparrow',
    130: 'Vesper_Sparrow',
    131: 'White_crowned_Sparrow',
    132: 'White_throated_Sparrow',
    133: 'Cape_Glossy_Starling',
    134: 'Bank_Swallow',
    135: 'Barn_Swallow',
    136: 'Cliff_Swallow',
    137: 'Tree_Swallow',
    138: 'Scarlet_Tanager',
    139: 'Summer_Tanager',
    140: 'Artic_Tern',
    141: 'Black_Tern',
    142: 'Caspian_Tern',
    143: 'Common_Tern',
    144: 'Elegant_Tern',
    145: 'Forsters_Tern',
    146: 'Least_Tern',
    147: 'Green_tailed_Towhee',
    148: 'Brown_Thrasher',
    149: 'Sage_Thrasher',
    150: 'Black_capped_Vireo',
    151: 'Blue_headed_Vireo',
    152: 'Philadelphia_Vireo',
    153: 'Red_eyed_Vireo',
    154: 'Warbling_Vireo',
    155: 'White_eyed_Vireo',
    156: 'Yellow_throated_Vireo',
    157: 'Bay_breasted_Warbler',
    158: 'Black_and_white_Warbler',
    159: 'Black_throated_Blue_Warbler',
    160: 'Blue_winged_Warbler',
    161: 'Canada_Warbler',
    162: 'Cape_May_Warbler',
    163: 'Cerulean_Warbler',
    164: 'Chestnut_sided_Warbler',
    165: 'Golden_winged_Warbler',
    166: 'Hooded_Warbler',
    167: 'Kentucky_Warbler',
    168: 'Magnolia_Warbler',
    169: 'Mourning_Warbler',
    170: 'Myrtle_Warbler',
    171: 'Nashville_Warbler',
    172: 'Orange_crowned_Warbler',
    173: 'Palm_Warbler',
    174: 'Pine_Warbler',
    175: 'Prairie_Warbler',
    176: 'Prothonotary_Warbler',
    177: 'Swainson_Warbler',
    178: 'Tennessee_Warbler',
    179: 'Wilson_Warbler',
    180: 'Worm_eating_Warbler',
    181: 'Yellow_Warbler',
    182: 'Northern_Waterthrush',
    183: 'Louisiana_Waterthrush',
    184: 'Bohemian_Waxwing',
    185: 'Cedar_Waxwing',
    186: 'American_Three_toed_Woodpecker',
    187: 'Pileated_Woodpecker',
    188: 'Red_bellied_Woodpecker',
    189: 'Red_cockaded_Woodpecker',
    190: 'Red_headed_Woodpecker',
    191: 'Downy_Woodpecker',
    192: 'Bewick_Wren',
    193: 'Cactus_Wren',
    194: 'Carolina_Wren',
    195: 'House_Wren',
    196: 'Marsh_Wren',
    197: 'Rock_Wren',
    198: 'Winter_Wren',
    199: 'Common_Yellowthroat'
}

# Function to create class directories with bird names and move images


def organize_images(txt_file, split):
    # Create the output directory if it doesn't exist
    output_dir = os.path.join(data_dir, split)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the txt file containing image paths and labels
    with open(txt_file, 'r') as f:
        for line in f:
            # Split each line by space to get image name and class label
            image_name, class_label = line.strip().split()
            class_label = int(class_label)

            # Get the corresponding bird species name for the label
            # Default to 'Unknown' if label not found
            bird_name = label_to_bird.get(class_label, 'Unknown')

            # Create a folder for the bird species if it doesn't exist
            class_dir = os.path.join(output_dir, bird_name)
            if not os.path.exists(class_dir):
                os.makedirs(class_dir)

            # Source image path
            src_path = os.path.join(data_dir, split, image_name)

            # Destination image path (class-specific folder with bird species name)
            dest_path = os.path.join(class_dir, image_name)

            # Move the image to the species folder
            shutil.move(src_path, dest_path)

            print(f"Moved {image_name} to {class_dir}")


# Organize training images
organize_images(train_txt, 'train')

# Organize test images
organize_images(test_txt, 'test')

print("Images organized successfully.")
