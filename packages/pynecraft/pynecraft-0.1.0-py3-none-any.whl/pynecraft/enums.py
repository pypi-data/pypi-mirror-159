"""Various enums for varoius groups of canstants. Most are generated automatically from the web pages at
minecraft.fandom.com."""

from enum import Enum

from typing import Tuple


class ValueEnum(Enum):
    def __str__(self):
        return self.value

    def __lt__(self, other):
        return self.value < other.value


# noinspection SpellCheckingInspection
class TeamOption(ValueEnum):
    DISPLAY_NAME = "displayName"
    """Set the display name of the team."""
    COLOR = "color"
    """Decide the color of the team and players in chat, above their head, on the Tab menu, and on the sidebar. Also changes the color of the outline of the entities caused by the Glowing effect."""
    FRIENDLY_FIRE = "friendlyFire"
    """Enable/Disable players inflicting damage on each other when on the same team. (Note: players can still inflict status effects on each other.) Does not affect some non-player entities in a team."""
    SEE_FRIENDLY_INVISIBLES = "seeFriendlyInvisibles"
    """Decide players can see invisible players on their team as whether semi-transparent or completely invisible."""
    NAMETAG_VISIBILITY = "nametagVisibility"
    """Decide whose name tags above their heads can be seen."""
    DEATH_MESSAGE_VISIBILITY = "deathMessageVisibility"
    """Control the visibility of death messages for players."""
    COLLISION_RULE = "collisionRule"
    """Controls the way the entities on the team collide with other entities."""
    PREFIX = "prefix"
    """Modifies the prefix that displays before players' names."""
    SUFFIX = "suffix"
    """Modifies the suffix that displays after players' names."""

    @staticmethod
    def value_spec(enum):
        return {"displayName": str, "color": str, "friendlyFire": bool, "seeFriendlyInvisibles": bool,
                "nametagVisibility": ['never', 'hideForOtherTeams', 'hideForOwnTeam', 'always'],
                "deathMessageVisibility": ['never', 'hideForOtherTeams', 'hideForOwnTeam', 'always'],
                "collisionRule": ['never', 'pushOtherTeams', 'pushOwnTeam', 'always'], "prefix": str, "suffix": str, }[
            enum.value]


# noinspection SpellCheckingInspection
class Pattern(ValueEnum):
    NONE = ''
    DOWN_RIGHT_STRIPE = 'drs'
    DOWN_LEFT_STRIPE = 'dls'
    CROSS = 'cr'
    BOTTOM_STRIPE = 'bs'
    MIDDLE_STRIPE = 'ms'
    TOP_STRIPE = 'ts'
    SQUARE_CROSS = 'sc'
    LEFT_STRIPE = 'ls'
    CENTER_STRIPE = 'cs'
    RIGHT_STRIPE = 'rs'
    SMALL_STRIPES = 'ss'
    LEFT_DIAGONAL = 'ld'
    RIGHT_UPSIDE_DOWN_DIAGONAL = 'rud'
    LEFT_UPSIDE_DOWN_DIAGONAL = 'lud'
    RIGHT_DIAGONAL = 'rd'
    VERTICAL_HALF_LEFT = 'vh'
    VERTICAL_HALF_RIGHT = 'vhr'
    HORIZONTAL_HALF_BOTTOM = 'hhb'
    HORIZONTAL_HALF_TOP = 'hh'
    BOTTOM_LEFT_CORNER = 'bl'
    BOTTOM_RIGHT_CORNER = 'br'
    TOP_LEFT_CORNER = 'tl'
    TOP_RIGHT_CORNER = 'tr'
    BOTTOM_TRIANGLE = 'bt'
    TOP_TRIANGLE = 'tt'
    BOTTOM_TRIANGLE_SAWTOOTH = 'bts'
    TOP_TRIANGLE_SAWTOOTH = 'tts'
    MIDDLE_CIRCLE = 'mc'
    MIDDLE_RHOMBUS = 'mr'
    BORDER = 'bo'
    CURLY_BORDER = 'cbo'
    GRADIENT = 'gra'
    GRADIENT_UPSIDE_DOWN = 'gru'
    CREEPER = 'cre'
    BRICK = 'bri'
    SKULL = 'sku'
    FLOWER = 'flo'
    MOJANG = 'moj'
    GLOBE = 'glb'
    PIG = 'pig'

    @staticmethod
    def sign_text(pattern) -> Tuple[str]:
        return {'': ('Blank',), 'drs': ('Down Right Stripe',), 'dls': ('Down Left Stripe',), 'cr': ('Cross',),
                'bs': ('Bottom Stripe',), 'ms': ('Middle Stripe',), 'ts': ('Top Stripe',), 'sc': ('Square Cross',),
                'ls': ('Left Stripe',), 'cs': ('Center Stripe',), 'rs': ('Right Stripe',), 'ss': ('Small Stripes',),
                'ld': ('Left Diagonal',), 'rud': ('Right Upside-Down', 'Diagonal',),
                'lud': ('Left Upside-Down', 'Diagonal',), 'rd': ('Right Diagonal',), 'vh': ('Vertical Half', '(Left)',),
                'vhr': ('Vertical Half', '(Right)',), 'hhb': ('Horizontal Half', '(Bottom)',),
                'hh': ('Horizontal Half', '(Top)',), 'bl': ('Bottom Left', 'Corner',),
                'br': ('Bottom Right', 'Corner',), 'tl': ('Top Left', 'Corner',), 'tr': ('Top Right', 'Corner',),
                'bt': ('Bottom Triangle',), 'tt': ('Top Triangle',), 'bts': ('Bottom Triangle', 'Sawtooth',),
                'tts': ('Top Triangle', 'Sawtooth',), 'mc': ('Middle Circle',), 'mr': ('Middle Rhombus',),
                'bo': ('Border',), 'cbo': ('Curly Border',), 'gra': ('Gradient',), 'gru': ('Gradient', 'Upside-Down',),
                'cre': ('Creeper',), 'bri': ('Brick',), 'sku': ('Skull',), 'flo': ('Flower',), 'moj': ('Mojang',),
                'glb': ('Globe',), 'pig': ('Pig',), }[pattern.value]


# Generated enums:


# noinspection SpellCheckingInspection
class Advancement(ValueEnum):
    MINECRAFT = "story/root"
    """The heart and story of the game."""
    STONE_AGE = "story/mine_stone"
    """Mine stone with your new pickaxe."""
    GETTING_AN_UPGRADE = "story/upgrade_tools"
    """Construct a better pickaxe."""
    ACQUIRE_HARDWARE = "story/smelt_iron"
    """Smelt an iron ingot."""
    SUIT_UP = "story/obtain_armor"
    """Protect yourself with a piece of iron armor."""
    HOT_STUFF = "story/lava_bucket"
    """Fill a bucket with lava."""
    ISNT_IT_IRON_PICK = "story/iron_tools"
    """Upgrade your pickaxe."""
    NOT_TODAY_THANK_YOU = "story/deflect_arrow"
    """Block a projectile using your shield."""
    ICE_BUCKET_CHALLENGE = "story/form_obsidian"
    """Obtain a block of obsidian."""
    DIAMONDS = "story/mine_diamond"
    """Acquire diamonds."""
    WE_NEED_TO_GO_DEEPER = "story/enter_the_nether"
    """Build, light and enter a Nether Portal."""
    COVER_ME_WITH_DIAMONDS = "story/shiny_gear"
    """Diamond armor saves lives."""
    ENCHANTER = "story/enchant_item"
    """Enchant an item at an Enchantment Table."""
    ZOMBIE_DOCTOR = "story/cure_zombie_villager"
    """Weaken and then cure a Zombie Villager."""
    EYE_SPY = "story/follow_ender_eye"
    """Follow an Ender Eye."""
    ENTER_THE_END = "story/enter_the_end"
    """Enter the End Portal."""
    NETHER = "nether/root"
    """Bring summer clothes."""
    RETURN_TO_SENDER = "nether/return_to_sender"
    """Destroy a Ghast with a fireball."""
    THOSE_WERE_THE_DAYS = "nether/find_bastion"
    """Enter a Bastion Remnant."""
    HIDDEN_IN_THE_DEPTHS = "nether/obtain_ancient_debris"
    """Obtain Ancient Debris."""
    SUBSPACE_BUBBLE = "nether/fast_travel"
    """Use the Nether to travel 7 km in the Overworld."""
    A_TERRIBLE_FORTRESS = "nether/find_fortress"
    """Break your way into a Nether Fortress."""
    WHO_IS_CUTTING_ONIONS = "nether/obtain_crying_obsidian"
    """Obtain Crying Obsidian."""
    OH_SHINY = "nether/distract_piglin"
    """Distract Piglins with gold."""
    THIS_BOAT_HAS_LEGS = "nether/ride_strider"
    """Ride a Strider with a Warped Fungus on a Stick."""
    UNEASY_ALLIANCE = "nether/uneasy_alliance"
    """Rescue a Ghast from the Nether, bring it safely home to the Overworld... and then kill it."""
    WAR_PIGS = "nether/loot_bastion"
    """Loot a chest in a Bastion Remnant."""
    COUNTRY_LODE_TAKE_ME_HOME = "nether/use_lodestone"
    """Use a compass on a Lodestone."""
    COVER_ME_IN_DEBRIS = "nether/netherite_armor"
    """Get a full suit of Netherite armor."""
    SPOOKY_SCARY_SKELETON = "nether/get_wither_skull"
    """Obtain a Wither Skeleton's skull."""
    INTO_FIRE = "nether/obtain_blaze_rod"
    """Relieve a Blaze of its rod."""
    NOT_QUITE_NINE_LIVES = "nether/charge_respawn_anchor"
    """Charge a Respawn Anchor to the maximum."""
    FEELS_LIKE_HOME = "nether/ride_strider_in_overworld_lava"
    """Take a Strider for a loooong ride on a lava lake in the Overworld."""
    HOT_TOURIST_DESTINATIONS = "nether/explore_nether"
    """Explore all Nether biomes."""
    WITHERING_HEIGHTS = "nether/summon_wither"
    """Summon the Wither."""
    LOCAL_BREWERY = "nether/brew_potion"
    """Brew a potion."""
    BRING_HOME_THE_BEACON = "nether/create_beacon"
    """Construct and place a beacon."""
    A_FURIOUS_COCKTAIL = "nether/all_potions"
    """Have every potion effect applied at the same time."""
    BEACONATOR = "nether/create_full_beacon"
    """Bring a beacon to full power."""
    HOW_DID_WE_GET_HERE = "nether/all_effects"
    """Have every effect applied at the same time."""
    THE_END = "end/root"
    """Or the beginning?"""
    FREE_THE_END = "end/kill_dragon"
    """Good luck."""
    THE_NEXT_GENERATION = "end/dragon_egg"
    """Hold the Dragon Egg."""
    REMOTE_GETAWAY = "end/enter_end_gateway"
    """Escape the island."""
    THE_END_AGAIN = "end/respawn_dragon"
    """Respawn the Ender Dragon."""
    YOU_NEED_A_MINT = "end/dragon_breath"
    """Collect dragon's breath in a glass bottle."""
    THE_CITY_AT_THE_END_OF_THE_GAME = "end/find_end_city"
    """Go on in, what could happen?"""
    SKYS_THE_LIMIT = "end/elytra"
    """Find elytra."""
    GREAT_VIEW_FROM_UP_HERE = "end/levitate"
    """Levitate up 50 blocks from the attacks of a Shulker."""
    ADVENTURE = "adventure/root"
    """Adventure, exploration, and combat."""
    VOLUNTARY_EXILE = "adventure/voluntary_exile"
    """Kill a raid captain.Maybe consider staying away from villages for the time being..."""
    IS_IT_A_BIRD = "adventure/spyglass_at_parrot"
    """Look at a parrot through a spyglass."""
    MONSTER_HUNTER = "adventure/kill_a_mob"
    """Kill any hostile monster."""
    WHAT_A_DEAL = "adventure/trade"
    """Successfully trade with a Villager."""
    STICKY_SITUATION = "adventure/honey_block_slide"
    """Jump into a Honey Block to break your fall."""
    OL_BETSY = "adventure/ol_betsy"
    """Shoot a crossbow."""
    SURGE_PROTECTOR = "adventure/lightning_rod_with_villager_no_fire"
    """Protect a villager from an undesired shock without starting a fire."""
    CAVES__CLIFFS = "adventure/fall_from_world_height"
    """Free fall from the top of the world (build limit) to the bottom of the world and survive."""
    SNEAK_100 = "adventure/avoid_vibration"
    """Sneak near a Sculk Sensor or Warden to prevent it from detecting you."""
    SWEET_DREAMS = "adventure/sleep_in_bed"
    """Sleep in a bed to change your respawn point."""
    HERO_OF_THE_VILLAGE = "adventure/hero_of_the_village"
    """Successfully defend a village from a raid."""
    IS_IT_A_BALLOON = "adventure/spyglass_at_ghast"
    """Look at a ghast through a spyglass."""
    A_THROWAWAY_JOKE = "adventure/throw_trident"
    """Throw a trident at something.Note: Throwing away your only weapon is not a good idea."""
    IT_SPREADS = "adventure/kill_mob_near_sculk_catalyst"
    """Kill a mob near a Sculk Catalyst."""
    TAKE_AIM = "adventure/shoot_arrow"
    """Shoot something with an arrow."""
    MONSTERS_HUNTED = "adventure/kill_all_mobs"
    """Kill one of every hostile monster."""
    POSTMORTAL = "adventure/totem_of_undying"
    """Use a Totem of Undying to cheat death."""
    HIRED_HELP = "adventure/summon_iron_golem"
    """Summon an Iron Golem to help defend a village."""
    STAR_TRADER = "adventure/trade_at_world_height"
    """Trade with a Villager at the build height limit."""
    TWO_BIRDS_ONE_ARROW = "adventure/two_birds_one_arrow"
    """Kill two Phantoms with a piercing arrow."""
    WHOS_THE_PILLAGER_NOW = "adventure/whos_the_pillager_now"
    """Give a Pillager a taste of their own medicine."""
    ARBALISTIC = "adventure/arbalistic"
    """Kill five unique mobs with one crossbow shot."""
    ADVENTURING_TIME = "adventure/adventuring_time"
    """Discover every biome."""
    SOUND_OF_MUSIC = "adventure/play_jukebox_in_meadows"
    """Make the Meadows come alive with the sound of music from a Jukebox."""
    LIGHT_AS_A_RABBIT = "adventure/walk_on_powder_snow_with_leather_boots"
    """Walk on powder snow...without sinking in it."""
    IS_IT_A_PLANE = "adventure/spyglass_at_dragon"
    """Look at the Ender Dragon through a spyglass."""
    VERY_VERY_FRIGHTENING = "adventure/very_very_frightening"
    """Strike a Villager with lightning."""
    SNIPER_DUEL = "adventure/sniper_duel"
    """Kill a Skeleton from at least 50 meters away."""
    BULLSEYE = "adventure/bullseye"
    """Hit the bullseye of a Target block from at least 30 meters away."""
    HUSBANDRY = "husbandry/root"
    """The world is full of friends and food."""
    BEE_OUR_GUEST = "husbandry/safely_harvest_honey"
    """Use a Campfire to collect Honey from a Beehive using a Bottle without aggravating the bees."""
    THE_PARROTS_AND_THE_BATS = "husbandry/breed_an_animal"
    """Breed two animals together."""
    YOUVE_GOT_A_FRIEND_IN_ME = "husbandry/allay_deliver_item_to_player"
    """Have an Allay deliver items to you."""
    WHATEVER_FLOATS_YOUR_GOAT = "husbandry/ride_a_boat_with_a_goat"
    """Get in a Boat and float with a Goat."""
    BEST_FRIENDS_FOREVER = "husbandry/tame_an_animal"
    """Tame an animal."""
    GLOW_AND_BEHOLD = "husbandry/make_a_sign_glow"
    """Make the text of a sign glow."""
    FISHY_BUSINESS = "husbandry/fishy_business"
    """Catch a fish."""
    TOTAL_BEELOCATION = "husbandry/silk_touch_nest"
    """Move a Bee Nest, with 3 bees inside, using Silk Touch."""
    BUKKIT_BUKKIT = "husbandry/tadpole_in_a_bucket"
    """Catch a Tadpole in a Bucket."""
    A_SEEDY_PLACE = "husbandry/plant_seed"
    """Plant a seed and watch it grow."""
    WAX_ON = "husbandry/wax_on"
    """Apply Honeycomb to a Copper block!"""
    TWO_BY_TWO = "husbandry/bred_all_animals"
    """Breed all the animals!"""
    BIRTHDAY_SONG = "husbandry/allay_deliver_cake_to_note_block"
    """Have an Allay drop a Cake at a Note Block."""
    A_COMPLETE_CATALOGUE = "husbandry/complete_catalogue"
    """Tame all cat variants!"""
    TACTICAL_FISHING = "husbandry/tactical_fishing"
    """Catch a fish... without a fishing rod!"""
    WHEN_THE_SQUAD_HOPS_INTO_TOWN = "husbandry/leash_all_frog_variants"
    """Get each Frog variant on a Lead."""
    A_BALANCED_DIET = "husbandry/balanced_diet"
    """Eat everything that is edible, even if it's not good for you."""
    SERIOUS_DEDICATION = "husbandry/obtain_netherite_hoe"
    """Use a Netherite Ingot to upgrade a hoe, and then reevaluate your life choices."""
    WAX_OFF = "husbandry/wax_off"
    """Scrape Wax off of a Copper block!"""
    THE_CUTEST_PREDATOR = "husbandry/axolotl_in_a_bucket"
    """Catch an axolotl in a bucket."""
    WITH_OUR_POWERS_COMBINED = "husbandry/froglights"
    """Have all Froglights in your inventory."""
    THE_HEALING_POWER_OF_FRIENDSHIP = "husbandry/kill_axolotl_target"
    """Team up with an axolotl and win a fight."""

    @staticmethod
    def display_name(elem) -> str:
        return {Advancement.MINECRAFT: "Minecraft", Advancement.STONE_AGE: "Stone Age",
                Advancement.GETTING_AN_UPGRADE: "Getting an Upgrade", Advancement.ACQUIRE_HARDWARE: "Acquire Hardware",
                Advancement.SUIT_UP: "Suit Up", Advancement.HOT_STUFF: "Hot Stuff",
                Advancement.ISNT_IT_IRON_PICK: "Isn't It Iron Pick",
                Advancement.NOT_TODAY_THANK_YOU: "Not Today, Thank You",
                Advancement.ICE_BUCKET_CHALLENGE: "Ice Bucket Challenge", Advancement.DIAMONDS: "Diamonds!",
                Advancement.WE_NEED_TO_GO_DEEPER: "We Need to Go Deeper",
                Advancement.COVER_ME_WITH_DIAMONDS: "Cover Me with Diamonds", Advancement.ENCHANTER: "Enchanter",
                Advancement.ZOMBIE_DOCTOR: "Zombie Doctor", Advancement.EYE_SPY: "Eye Spy",
                Advancement.ENTER_THE_END: "The End?", Advancement.NETHER: "Nether",
                Advancement.RETURN_TO_SENDER: "Return to Sender",
                Advancement.THOSE_WERE_THE_DAYS: "Those Were the Days",
                Advancement.HIDDEN_IN_THE_DEPTHS: "Hidden in the Depths",
                Advancement.SUBSPACE_BUBBLE: "Subspace Bubble", Advancement.A_TERRIBLE_FORTRESS: "A Terrible Fortress",
                Advancement.WHO_IS_CUTTING_ONIONS: "Who is Cutting Onions?", Advancement.OH_SHINY: "Oh Shiny",
                Advancement.THIS_BOAT_HAS_LEGS: "This Boat Has Legs", Advancement.UNEASY_ALLIANCE: "Uneasy Alliance",
                Advancement.WAR_PIGS: "War Pigs", Advancement.COUNTRY_LODE_TAKE_ME_HOME: "Country Lode, Take Me Home",
                Advancement.COVER_ME_IN_DEBRIS: "Cover Me in Debris",
                Advancement.SPOOKY_SCARY_SKELETON: "Spooky Scary Skeleton", Advancement.INTO_FIRE: "Into Fire",
                Advancement.NOT_QUITE_NINE_LIVES: "Not Quite \"Nine\" Lives",
                Advancement.FEELS_LIKE_HOME: "Feels Like Home",
                Advancement.HOT_TOURIST_DESTINATIONS: "Hot Tourist Destinations",
                Advancement.WITHERING_HEIGHTS: "Withering Heights", Advancement.LOCAL_BREWERY: "Local Brewery",
                Advancement.BRING_HOME_THE_BEACON: "Bring Home the Beacon",
                Advancement.A_FURIOUS_COCKTAIL: "A Furious Cocktail", Advancement.BEACONATOR: "Beaconator",
                Advancement.HOW_DID_WE_GET_HERE: "How Did We Get Here?", Advancement.THE_END: "The End?",
                Advancement.FREE_THE_END: "Free the End", Advancement.THE_NEXT_GENERATION: "The Next Generation",
                Advancement.REMOTE_GETAWAY: "Remote Getaway", Advancement.THE_END_AGAIN: "The End... Again...",
                Advancement.YOU_NEED_A_MINT: "You Need a Mint",
                Advancement.THE_CITY_AT_THE_END_OF_THE_GAME: "The City at the End of the Game",
                Advancement.SKYS_THE_LIMIT: "Sky's the Limit",
                Advancement.GREAT_VIEW_FROM_UP_HERE: "Great View From Up Here", Advancement.ADVENTURE: "Adventure",
                Advancement.VOLUNTARY_EXILE: "Voluntary Exile", Advancement.IS_IT_A_BIRD: "Is It a Bird?",
                Advancement.MONSTER_HUNTER: "Monster Hunter", Advancement.WHAT_A_DEAL: "What a Deal!",
                Advancement.STICKY_SITUATION: "Sticky Situation", Advancement.OL_BETSY: "Ol' Betsy",
                Advancement.SURGE_PROTECTOR: "Surge Protector", Advancement.CAVES__CLIFFS: "Caves & Cliffs",
                Advancement.SNEAK_100: "Sneak 100", Advancement.SWEET_DREAMS: "Sweet Dreams",
                Advancement.HERO_OF_THE_VILLAGE: "Hero of the Village", Advancement.IS_IT_A_BALLOON: "Is It a Balloon?",
                Advancement.A_THROWAWAY_JOKE: "A Throwaway Joke", Advancement.IT_SPREADS: "It Spreads",
                Advancement.TAKE_AIM: "Take Aim", Advancement.MONSTERS_HUNTED: "Monsters Hunted",
                Advancement.POSTMORTAL: "Postmortal", Advancement.HIRED_HELP: "Hired Help",
                Advancement.STAR_TRADER: "Star Trader", Advancement.TWO_BIRDS_ONE_ARROW: "Two Birds, One Arrow",
                Advancement.WHOS_THE_PILLAGER_NOW: "Who's the Pillager Now?", Advancement.ARBALISTIC: "Arbalistic",
                Advancement.ADVENTURING_TIME: "Adventuring Time", Advancement.SOUND_OF_MUSIC: "Sound of Music",
                Advancement.LIGHT_AS_A_RABBIT: "Light as a Rabbit", Advancement.IS_IT_A_PLANE: "Is It a Plane?",
                Advancement.VERY_VERY_FRIGHTENING: "Very Very Frightening", Advancement.SNIPER_DUEL: "Sniper Duel",
                Advancement.BULLSEYE: "Bullseye", Advancement.HUSBANDRY: "Husbandry",
                Advancement.BEE_OUR_GUEST: "Bee Our Guest",
                Advancement.THE_PARROTS_AND_THE_BATS: "The Parrots and the Bats",
                Advancement.YOUVE_GOT_A_FRIEND_IN_ME: "You've Got a Friend in Me",
                Advancement.WHATEVER_FLOATS_YOUR_GOAT: "Whatever Floats Your Goat!",
                Advancement.BEST_FRIENDS_FOREVER: "Best Friends Forever",
                Advancement.GLOW_AND_BEHOLD: "Glow and Behold!", Advancement.FISHY_BUSINESS: "Fishy Business",
                Advancement.TOTAL_BEELOCATION: "Total Beelocation", Advancement.BUKKIT_BUKKIT: "Bukkit Bukkit",
                Advancement.A_SEEDY_PLACE: "A Seedy Place", Advancement.WAX_ON: "Wax On",
                Advancement.TWO_BY_TWO: "Two by Two", Advancement.BIRTHDAY_SONG: "Birthday Song",
                Advancement.A_COMPLETE_CATALOGUE: "A Complete Catalogue",
                Advancement.TACTICAL_FISHING: "Tactical Fishing",
                Advancement.WHEN_THE_SQUAD_HOPS_INTO_TOWN: "When the Squad Hops into Town",
                Advancement.A_BALANCED_DIET: "A Balanced Diet", Advancement.SERIOUS_DEDICATION: "Serious Dedication",
                Advancement.WAX_OFF: "Wax Off", Advancement.THE_CUTEST_PREDATOR: "The Cutest Predator",
                Advancement.WITH_OUR_POWERS_COMBINED: "With Our Powers Combined!",
                Advancement.THE_HEALING_POWER_OF_FRIENDSHIP: "The Healing Power of Friendship!"}[elem]


# noinspection SpellCheckingInspection
class Effect(ValueEnum):
    SPEED = "speed"
    """Increases walking speed; higher levels make the affected entity faster and increases the player's field of view when affected."""
    SLOWNESS = "slowness"
    """Decreases walking speed; higher levels make the affected entity slower and decreases the player's field of view when affected."""
    HASTE = "haste"
    """Increases mining and attack speed, higher levels increase the player's mining and attack speed."""
    MINING_FATIGUE = "mining_fatigue"
    """Decreases mining and attack speed, higher levels decrease the player's mining and attack speed."""
    STRENGTH = "strength"
    """Increases melee damage, higher levels make the affected entity do more melee damage."""
    INSTANT_HEALTH = "instant_health"
    """Heals living entities, damages undead, higher levels heal more health and do more damage."""
    INSTANT_DAMAGE = "instant_damage"
    """Damages living entities, heals undead, higher levels do more damage and heal more health."""
    JUMP_BOOST = "jump_boost"
    """Increases jump height and reduces fall damage, higher levels make the affected entity jump higher and reduces more fall damage."""
    NAUSEA = "nausea"
    """Wobbles and warps the screen."""
    REGENERATION = "regeneration"
    """Regenerates health over time, higher levels make health regenerate quicker."""
    RESISTANCE = "resistance"
    """Reduces damage, higher levels reduce more damage."""
    FIRE_RESISTANCE = "fire_resistance"
    """Prevents the affected entity from taking damage due to Fire, lava and other sources of fire damage."""
    WATER_BREATHING = "water_breathing"
    """Prevents drowning and lets the affected entity breathe underwater."""
    INVISIBILITY = "invisibility"
    """Grants invisibility, making the affected entity invisible (but not the item they hold or the armor they wear), and reduces other mobs' detection range for the affected entity, higher levels reduce other mobs' detection range more."""
    BLINDNESS = "blindness"
    """Impairs vision and disables the ability to sprint and critical hit."""
    NIGHT_VISION = "night_vision"
    """Lets the player see well in darkness and underwater."""
    HUNGER = "hunger"
    """Increases food exhaustion, higher levels cause the player to starve quicker."""
    WEAKNESS = "weakness"
    """Decreases melee damage, higher levels decrease more melee damage."""
    POISON = "poison"
    """Inflicts damage over time (but can't kill), higher levels do more damage per second, doesn't affect undead."""
    WITHER = "wither"
    """Inflicts damage over time (can kill), higher levels do more damage per second."""
    HEALTH_BOOST = "health_boost"
    """Increases maximum health, higher levels give the affected entity more maximum health."""
    ABSORPTION = "absorption"
    """Adds damage absorption (additional hearts that can't be regenerated), higher levels give more absorption."""
    SATURATION = "saturation"
    """Restores hunger and saturation."""
    GLOWING = "glowing"
    """Outlines the affected entity (can be seen through blocks)."""
    LEVITATION = "levitation"
    """Floats the affected entity upward."""
    LUCK = "luck"
    """Can increase chances of high-quality and more loot, higher levels increase the chances of better loot."""
    BAD_LUCK = "unluck"
    """Can reduce chances of high-quality and more loot, higher levels reduce the chance of good loot."""
    SLOW_FALLING = "slow_falling"
    """Decreases falling speed and negates fall damage."""
    CONDUIT_POWER = "conduit_power"
    """Increases underwater visibility and mining speed, prevents drowning."""
    DOLPHINS_GRACE = "dolphins_grace"
    """Increases swimming speed (only obtainable from dolphins)."""
    BAD_OMEN = "bad_omen"
    """Causes an illager raid to start upon entering a village (only received from an Illager captain upon its death), higher levels cause a more difficult raid."""
    HERO_OF_THE_VILLAGE = "hero_of_the_village"
    """Gives discounts on trades with villagers, and makes villagers throw items at the player depending on their profession."""
    DARKNESS = "darkness"
    """Darkens the players screen."""

    @staticmethod
    def display_name(elem) -> str:
        return {Effect.SPEED: "Speed", Effect.SLOWNESS: "Slowness", Effect.HASTE: "Haste",
                Effect.MINING_FATIGUE: "Mining Fatigue", Effect.STRENGTH: "Strength",
                Effect.INSTANT_HEALTH: "Instant Health", Effect.INSTANT_DAMAGE: "Instant Damage",
                Effect.JUMP_BOOST: "Jump Boost", Effect.NAUSEA: "Nausea", Effect.REGENERATION: "Regeneration",
                Effect.RESISTANCE: "Resistance", Effect.FIRE_RESISTANCE: "Fire Resistance",
                Effect.WATER_BREATHING: "Water Breathing", Effect.INVISIBILITY: "Invisibility",
                Effect.BLINDNESS: "Blindness", Effect.NIGHT_VISION: "Night Vision", Effect.HUNGER: "Hunger",
                Effect.WEAKNESS: "Weakness", Effect.POISON: "Poison", Effect.WITHER: "Wither",
                Effect.HEALTH_BOOST: "Health Boost", Effect.ABSORPTION: "Absorption", Effect.SATURATION: "Saturation",
                Effect.GLOWING: "Glowing", Effect.LEVITATION: "Levitation", Effect.LUCK: "Luck",
                Effect.BAD_LUCK: "Bad Luck", Effect.SLOW_FALLING: "Slow Falling", Effect.CONDUIT_POWER: "Conduit Power",
                Effect.DOLPHINS_GRACE: "Dolphin's Grace", Effect.BAD_OMEN: "Bad Omen",
                Effect.HERO_OF_THE_VILLAGE: "Hero of the Village", Effect.DARKNESS: "Darkness"}[elem]

    @staticmethod
    def negative(effect):
        return effect.value in ['blindness', 'darkness', 'hunger', 'instant_damage', 'mining_fatigue', 'nausea',
                                'poison', 'slowness', 'unluck', 'weakness', 'wither']


# noinspection SpellCheckingInspection
class Enchantment(ValueEnum):
    AQUA_AFFINITY = "aqua_affinity"
    """Increases underwater mining speed."""
    BANE_OF_ARTHROPODS = "bane_of_arthropods"
    """Increases damage and applies Slowness IV to arthropod mobs (spiders, cave spiders, silverfish, endermites and bees)."""
    BLAST_PROTECTION = "blast_protection"
    """Reduces explosion damage and knockback."""
    CHANNELING = "channeling"
    """During thunderstorms, tridents can strike enemies with a lightning bolt."""
    CLEAVING = "cleaving"
    """Increases damage and shield stunning."""
    CURSE_OF_BINDING = "curse_of_binding"
    """Items cannot be removed from armor slots."""
    CURSE_OF_VANISHING = "curse_of_vanishing"
    """Item disappears on death."""
    DEPTH_STRIDER = "depth_strider"
    """Increases underwater movement speed."""
    EFFICIENCY = "efficiency"
    """Increases tool speed, as well as the chance for axes to disable shields."""
    FEATHER_FALLING = "feather_falling"
    """Reduces fall damage."""
    FIRE_ASPECT = "fire_aspect"
    """Sets target on fire."""
    FIRE_PROTECTION = "fire_protection"
    """Reduces fire damage and burn time.Mutually exclusive with other protections."""
    FLAME = "flame"
    """Arrows shot are ignited and deal fire damage to the target."""
    FORTUNE = "fortune"
    """Increases the amount of block drops."""
    FROST_WALKER = "frost_walker"
    """Allows the player to walk on water by freezing the water under their feet."""
    IMPALING = "impaling"
    """Increases damage against aquatic mobs. In Bedrock Edition, increases damage against mobs in water or rain."""
    INFINITY = "infinity"
    """Prevents consumption of arrows."""
    KNOCKBACK = "knockback"
    """Increases knockback."""
    LOOTING = "looting"
    """Increases mob loot."""
    LOYALTY = "loyalty"
    """Trident returns after being thrown."""
    LUCK_OF_THE_SEA = "luck_of_the_sea"
    """Increases rate of good loot (enchanting books, etc.)."""
    LURE = "lure"
    """Decreases time for bites."""
    MENDING = "mending"
    """Repairs the item using experience."""
    MULTISHOT = "multishot"
    """Fires 3 arrows at the same time."""
    PIERCING = "piercing"
    """Arrows pierce entities, allowing for arrows to pierce through stacks of mobs. Available only to the crossbow."""
    POWER = "power"
    """Increases arrow damage."""
    PROJECTILE_PROTECTION = "projectile_protection"
    """Reduces damage from projectiles."""
    PROTECTION = "protection"
    """Reduces generic damage."""
    PUNCH = "punch"
    """Increases arrow knockback."""
    QUICK_CHARGE = "quick_charge"
    """Decreases crossbow charging time."""
    RESPIRATION = "respiration"
    """Extends underwater breathing time."""
    RIPTIDE = "riptide"
    """Trident launches player with itself when thrown while in water or rain."""
    SHARPNESS = "sharpness"
    """Increases melee damage."""
    SILK_TOUCH = "silk_touch"
    """Mined blocks drop themselves."""
    SMITE = "smite"
    """Increases damage to the undead."""
    SOUL_SPEED = "soul_speed"
    """Increases movement speed on soul soil."""
    SWEEPING_EDGE = "sweeping_edge"
    """Increases sweeping attack damage."""
    SWIFT_SNEAK = "swift_sneak"
    """Increases sneaking speed."""
    THORNS = "thorns"
    """Taking damage causes the attacker to also take damage."""
    UNBREAKING = "unbreaking"
    """Reduces durability damage."""

    @staticmethod
    def display_name(elem) -> str:
        return {Enchantment.AQUA_AFFINITY: "Aqua Affinity", Enchantment.BANE_OF_ARTHROPODS: "Bane of Arthropods",
                Enchantment.BLAST_PROTECTION: "Blast Protection", Enchantment.CHANNELING: "Channeling",
                Enchantment.CLEAVING: "Cleaving", Enchantment.CURSE_OF_BINDING: "Curse of Binding",
                Enchantment.CURSE_OF_VANISHING: "Curse of Vanishing", Enchantment.DEPTH_STRIDER: "Depth Strider",
                Enchantment.EFFICIENCY: "Efficiency", Enchantment.FEATHER_FALLING: "Feather Falling",
                Enchantment.FIRE_ASPECT: "Fire Aspect", Enchantment.FIRE_PROTECTION: "Fire Protection",
                Enchantment.FLAME: "Flame", Enchantment.FORTUNE: "Fortune", Enchantment.FROST_WALKER: "Frost Walker",
                Enchantment.IMPALING: "Impaling", Enchantment.INFINITY: "Infinity", Enchantment.KNOCKBACK: "Knockback",
                Enchantment.LOOTING: "Looting", Enchantment.LOYALTY: "Loyalty",
                Enchantment.LUCK_OF_THE_SEA: "Luck of the Sea", Enchantment.LURE: "Lure",
                Enchantment.MENDING: "Mending", Enchantment.MULTISHOT: "Multishot", Enchantment.PIERCING: "Piercing",
                Enchantment.POWER: "Power", Enchantment.PROJECTILE_PROTECTION: "Projectile Protection",
                Enchantment.PROTECTION: "Protection", Enchantment.PUNCH: "Punch",
                Enchantment.QUICK_CHARGE: "Quick Charge", Enchantment.RESPIRATION: "Respiration",
                Enchantment.RIPTIDE: "Riptide", Enchantment.SHARPNESS: "Sharpness",
                Enchantment.SILK_TOUCH: "Silk Touch", Enchantment.SMITE: "Smite", Enchantment.SOUL_SPEED: "Soul Speed",
                Enchantment.SWEEPING_EDGE: "Sweeping Edge", Enchantment.SWIFT_SNEAK: "Swift Sneak",
                Enchantment.THORNS: "Thorns", Enchantment.UNBREAKING: "Unbreaking"}[elem]

    @staticmethod
    def max_level(ench):
        return {'aqua_affinity': 1, 'bane_of_arthropods': 5, 'blast_protection': 4, 'channeling': 1, 'cleaving': 3,
                'curse_of_binding': 1, 'curse_of_vanishing': 1, 'depth_strider': 3, 'efficiency': 5,
                'feather_falling': 4, 'fire_aspect': 2, 'fire_protection': 4, 'flame': 1, 'fortune': 3,
                'frost_walker': 2, 'impaling': 5, 'infinity': 1, 'knockback': 2, 'looting': 3, 'loyalty': 3,
                'luck_of_the_sea': 3, 'lure': 3, 'mending': 1, 'multishot': 1, 'piercing': 4, 'power': 5,
                'projectile_protection': 4, 'protection': 4, 'punch': 2, 'quick_charge': 3, 'respiration': 3,
                'riptide': 3, 'sharpness': 5, 'silk_touch': 1, 'smite': 5, 'soul_speed': 3, 'sweeping_edge': 3,
                'swift_sneak': 3, 'thorns': 3, 'unbreaking': 3}[ench.value]


# noinspection SpellCheckingInspection
class GameRule(ValueEnum):
    ANNOUNCE_ADVANCEMENTS = "announceAdvancements"
    """Whether advancements should be announced in chat."""
    COMMAND_BLOCK_OUTPUT = "commandBlockOutput"
    """Whether command blocks should notify admins when they perform commands."""
    DISABLE_ELYTRA_MOVEMENT_CHECK = "disableElytraMovementCheck"
    """Whether the server should skip checking player speed when the player is wearing elytra. Often helps with jittering due to lag in multiplayer."""
    DISABLE_RAIDS = "disableRaids"
    """Whether raids are disabled."""
    DO_DAYLIGHT_CYCLE = "doDaylightCycle"
    """Whether the daylight cycle and moon phases progress."""
    DO_ENTITY_DROPS = "doEntityDrops"
    """Whether entities that are not mobs should have drops."""
    DO_FIRE_TICK = "doFireTick"
    """Whether fire should spread and naturally extinguish."""
    DO_INSOMNIA = "doInsomnia"
    """Whether phantoms can spawn in the nighttime."""
    DO_IMMEDIATE_RESPAWN = "doImmediateRespawn"
    """Players respawn immediately without showing the death screen."""
    DO_LIMITED_CRAFTING = "doLimitedCrafting"
    """Whether players should be able to craft only those recipes that they've unlocked first."""
    DO_MOB_LOOT = "doMobLoot"
    """Whether mobs should drop items and experience orbs."""
    DO_MOB_SPAWNING = "doMobSpawning"
    """Whether mobs should naturally spawn. Does not affect monster spawners."""
    DO_PATROL_SPAWNING = "doPatrolSpawning"
    """Whether patrols can spawn."""
    DO_TILE_DROPS = "doTileDrops"
    """Whether blocks should have drops."""
    DO_TRADER_SPAWNING = "doTraderSpawning"
    """Whether wandering traders can spawn."""
    DO_WEATHER_CYCLE = "doWeatherCycle"
    """Whether the weather can change naturally. The /weather command can still change weather."""
    DO_WARDEN_SPAWNING = "doWardenSpawning"
    """Whether wardens can spawn."""
    DROWNING_DAMAGE = "drowningDamage"
    """Whether the player should take damage when drowning."""
    FALL_DAMAGE = "fallDamage"
    """Whether the player should take fall damage."""
    FIRE_DAMAGE = "fireDamage"
    """Whether the player should take damage in fire, lava, campfires, or on magma blocks."""
    FORGIVE_DEAD_PLAYERS = "forgiveDeadPlayers"
    """Makes angered neutral mobs stop being angry when the targeted player dies nearby."""
    FREEZE_DAMAGE = "freezeDamage"
    """Whether the player should take damage when inside powder snow."""
    KEEP_INVENTORY = "keepInventory"
    """Whether the player should keep items and experience in their inventory after death."""
    LOG_ADMIN_COMMANDS = "logAdminCommands"
    """Whether to log admin commands to server log."""
    MAX_COMMAND_CHAIN_LENGTH = "maxCommandChainLength"
    """The maximum length of a chain of commands that can be executed during one tick. Applies to command blocks and functions."""
    MAX_ENTITY_CRAMMING = "maxEntityCramming"
    """The maximum number of pushable entities a mob or player can push, before taking 3 suffocation damage per half-second. Setting to 0 or lower disables the rule. Damage affects survival-mode or adventure-mode players, and all mobs but bats. Pushable entities include non-spectator-mode players, any mob except bats, as well as boats and minecarts."""
    MOB_GRIEFING = "mobGriefing"
    """Whether creepers, zombies, endermen, ghasts, withers, ender dragons, rabbits, sheep, villagers, silverfish, snow golems, and end crystals should be able to change blocks, and whether mobs can pick up items. When mobGriefing is disabled, piglins will not pick up gold ingots, but a player can still barter with them by using the item on the mob. Similarly, villagers will not pick up food items but can still breed until they run out of any food already in their inventory. This also affects the capability of zombie-like creatures like zombified piglins and drowned to pathfind to turtle eggs."""
    NATURAL_REGENERATION = "naturalRegeneration"
    """Whether the player can regenerate health naturally if their hunger is full enough (doesn't affect external healing, such as golden apples, the Regeneration effect, etc.)."""
    PLAYERS_SLEEPING_PERCENTAGE = "playersSleepingPercentage"
    """What percentage of players must sleep to skip the night."""
    RANDOM_TICK_SPEED = "randomTickSpeed"
    """How often a random block tick occurs (such as plant growth, leaf decay, etc.) per chunk section per game tick. 0 and negative values disables random ticks, higher numbers increase random ticks. Setting to a high integer results in high speeds of decay and growth. Numbers over 4096 make plant growth or leaf decay instantaneous."""
    REDUCED_DEBUG_INFO = "reducedDebugInfo"
    """Whether the debug screen shows all or reduced information; and whether the effects of F3 + B (entity hitboxes) and F3 + G (chunk boundaries) are shown."""
    SEND_COMMAND_FEEDBACK = "sendCommandFeedback"
    """Whether the feedback from commands executed by a player should show up in chat. Also affects the default behavior of whether command blocks store their output text."""
    SHOW_DEATH_MESSAGES = "showDeathMessages"
    """Whether death messages are put into chat when a player dies. Also affects whether a message is sent to the pet's owner when the pet dies."""
    SPAWN_RADIUS = "spawnRadius"
    """The number of blocks outward from the world spawn coordinates that a player spawns in when first joining a server or when dying without a personal spawnpoint. Has no effect on servers where the default game mode is adventure."""
    SPECTATORS_GENERATE_CHUNKS = "spectatorsGenerateChunks"
    """Whether players in spectator mode can generate chunks."""
    UNIVERSAL_ANGER = "universalAnger"
    """Makes angered neutral mobs attack any nearby player, not just the player that angered them. Works best if forgiveDeadPlayers is disabled."""

    @staticmethod
    def display_name(elem) -> str:
        return \
            {GameRule.ANNOUNCE_ADVANCEMENTS: "announce Advancements",
             GameRule.COMMAND_BLOCK_OUTPUT: "command Block Output",
             GameRule.DISABLE_ELYTRA_MOVEMENT_CHECK: "disable Elytra Movement Check",
             GameRule.DISABLE_RAIDS: "disable Raids", GameRule.DO_DAYLIGHT_CYCLE: "do Daylight Cycle",
             GameRule.DO_ENTITY_DROPS: "do Entity Drops", GameRule.DO_FIRE_TICK: "do Fire Tick",
             GameRule.DO_INSOMNIA: "do Insomnia", GameRule.DO_IMMEDIATE_RESPAWN: "do Immediate Respawn",
             GameRule.DO_LIMITED_CRAFTING: "do Limited Crafting", GameRule.DO_MOB_LOOT: "do Mob Loot",
             GameRule.DO_MOB_SPAWNING: "do Mob Spawning", GameRule.DO_PATROL_SPAWNING: "do Patrol Spawning",
             GameRule.DO_TILE_DROPS: "do Tile Drops", GameRule.DO_TRADER_SPAWNING: "do Trader Spawning",
             GameRule.DO_WEATHER_CYCLE: "do Weather Cycle", GameRule.DO_WARDEN_SPAWNING: "do Warden Spawning",
             GameRule.DROWNING_DAMAGE: "drowning Damage", GameRule.FALL_DAMAGE: "fall Damage",
             GameRule.FIRE_DAMAGE: "fire Damage", GameRule.FORGIVE_DEAD_PLAYERS: "forgive Dead Players",
             GameRule.FREEZE_DAMAGE: "freeze Damage", GameRule.KEEP_INVENTORY: "keep Inventory",
             GameRule.LOG_ADMIN_COMMANDS: "log Admin Commands",
             GameRule.MAX_COMMAND_CHAIN_LENGTH: "max Command Chain Length",
             GameRule.MAX_ENTITY_CRAMMING: "max Entity Cramming", GameRule.MOB_GRIEFING: "mob Griefing",
             GameRule.NATURAL_REGENERATION: "natural Regeneration",
             GameRule.PLAYERS_SLEEPING_PERCENTAGE: "players Sleeping Percentage",
             GameRule.RANDOM_TICK_SPEED: "random Tick Speed", GameRule.REDUCED_DEBUG_INFO: "reduced Debug Info",
             GameRule.SEND_COMMAND_FEEDBACK: "send Command Feedback",
             GameRule.SHOW_DEATH_MESSAGES: "show Death Messages",
             GameRule.SPAWN_RADIUS: "spawn Radius", GameRule.SPECTATORS_GENERATE_CHUNKS: "spectators Generate Chunks",
             GameRule.UNIVERSAL_ANGER: "universal Anger"}[elem]

    @staticmethod
    def rule_type(rule):
        return {'announceAdvancements': 'bool', 'commandBlockOutput': 'bool', 'disableElytraMovementCheck': 'bool',
                'disableRaids': 'bool', 'doDaylightCycle': 'bool', 'doEntityDrops': 'bool', 'doFireTick': 'bool',
                'doInsomnia': 'bool', 'doImmediateRespawn': 'bool', 'doLimitedCrafting': 'bool', 'doMobLoot': 'bool',
                'doMobSpawning': 'bool', 'doPatrolSpawning': 'bool', 'doTileDrops': 'bool', 'doTraderSpawning': 'bool',
                'doWeatherCycle': 'bool', 'doWardenSpawning': 'bool', 'drowningDamage': 'bool', 'fallDamage': 'bool',
                'fireDamage': 'bool', 'forgiveDeadPlayers': 'bool', 'freezeDamage': 'bool', 'keepInventory': 'bool',
                'logAdminCommands': 'bool', 'maxCommandChainLength': 'int', 'maxEntityCramming': 'int',
                'mobGriefing': 'bool', 'naturalRegeneration': 'bool', 'playersSleepingPercentage': 'int',
                'randomTickSpeed': 'int', 'reducedDebugInfo': 'bool', 'sendCommandFeedback': 'bool',
                'showDeathMessages': 'bool', 'spawnRadius': 'int', 'spectatorsGenerateChunks': 'bool',
                'universalAnger': 'bool'}[rule.value]


# noinspection SpellCheckingInspection
class ScoreCriteria(ValueEnum):
    DUMMY = "dummy"
    """Score is only changed by commands, and not by game events such as death. This is useful for event flags, state mappings, currencies,..."""
    TRIGGER = "trigger"
    """Score is only changed by commands, and not by game events such as death. The /trigger command can be used by a player to set or increment/decrement their own score in an objective with this criterion. The /trigger command fails if the objective has not been "enabled" for the player using it, and the objective is disabled for the player after using the /trigger command on it. Note that the /trigger command can be used by ordinary players even if Cheats are off and they are not an Operator. This is useful for player input via /tellraw interfaces."""
    DEATH_COUNT = "deathCount"
    """Score increments automatically for a player when they die."""
    PLAYER_KILL_COUNT = "playerKillCount"
    """Score increments automatically for a player when they kill another player."""
    TOTAL_KILL_COUNT = "totalKillCount"
    """Score increments automatically for a player when they kill another player or a mob."""
    HEALTH = "health"
    """Ranges from 0 to 20 on a normal player; represents the amount of half-hearts the player has. May appear as 0 for players before their health has changed for the first time. Extra hearts and absorption hearts also count to the health score, meaning that with Attributes/Modifiers or the Health Boost or Absorption status effects, health can far surpass 20."""
    XP = "xp"
    """Matches the total amount of experience the player has collected since their last death (or in other words, their score)."""
    LEVEL = "level"
    """Matches the current experience level of the player."""
    FOOD = "food"
    """Ranges from 0 to 20; represents the amount of hunger points the player has. May appear as 0 for players before their foodLevel has changed for the first time."""
    AIR = "air"
    """Ranges from 0 to 300; represents the amount of air the player has left from swimming under water, matches the air nbt tag of the player."""
    ARMOR = "armor"
    """Ranges from 0 to 20; represents the amount of armor points the player has. May appear as 0 for players before their armor has changed for the first time."""

    @staticmethod
    def display_name(elem) -> str:
        return \
            {ScoreCriteria.DUMMY: "dummy", ScoreCriteria.TRIGGER: "trigger", ScoreCriteria.DEATH_COUNT: "death Count",
             ScoreCriteria.PLAYER_KILL_COUNT: "player Kill Count", ScoreCriteria.TOTAL_KILL_COUNT: "total Kill Count",
             ScoreCriteria.HEALTH: "health", ScoreCriteria.XP: "xp", ScoreCriteria.LEVEL: "level",
             ScoreCriteria.FOOD: "food", ScoreCriteria.AIR: "air", ScoreCriteria.ARMOR: "armor"}[elem]


# noinspection SpellCheckingInspection
class Particle(ValueEnum):
    AMBIENT_ENTITY_EFFECT = "ambient_entity_effect"
    """Beacon effects."""
    ANGRY_VILLAGER = "angry_villager"
    """Attacking a villager in a village; when villagers can't breed because there aren't enough beds nearby or when a panda is attacked by a player on the village."""
    ASH = "ash"
    """Naturally generated in soul sand valley biome environment."""
    BARRIER = "barrier"
    """Barrier blocks."""
    BLOCK = "block"
    """Breaking blocks, sprinting, iron golems walking."""
    BLOCK_MARKER = "block_marker"
    """Replaces separate barrier and light particles in 1.19."""
    BUBBLE = "bubble"
    """Entities in water, guardian laser beams, fishing."""
    BUBBLE_COLUMN_UP = "bubble_column_up"
    """Upward bubble columns made by soul sand under water."""
    BUBBLE_POP = "bubble_pop"
    """Unused."""
    CAMPFIRE_COSY_SMOKE = "campfire_cosy_smoke"
    """Smoke produced by campfires and soul campfires."""
    CAMPFIRE_SIGNAL_SMOKE = "campfire_signal_smoke"
    """Smoke produced by campfires and soul campfires when above a hay bale."""
    CLOUD = "cloud"
    """After jumping into water while on fire in Bedrock Edition or an entity dies in Java Edition."""
    COMPOSTER = "composter"
    """Filling a composter."""
    CRIMSON_SPORE = "crimson_spore"
    """A crimson particle generated in crimson forest biome environment."""
    CRIT = "crit"
    """Critical hits, fully charged bow shots, crossbows, evoker fangs."""
    CURRENT_DOWN = "current_down"
    """Bubble column whirlpools made by magma blocks underwater."""
    DAMAGE_INDICATOR = "damage_indicator"
    """From mobs and players when hurt by a melee attack."""
    DOLPHIN = "dolphin"
    """Trails behind swimming dolphins."""
    DRAGON_BREATH = "dragon_breath"
    """An ender dragon's breath and dragon fireballs."""
    DRIPPING_DRIPSTONE_LAVA = "dripping_dripstone_lava"
    """Dripping lava from the pointed dripstone."""
    DRIPPING_DRIPSTONE_WATER = "dripping_dripstone_water"
    """Dripping water from the pointed dripstone."""
    DRIPPING_HONEY = "dripping_honey"
    """Dripping honey through blocks that haven't dripped down yet."""
    DRIPPING_LAVA = "dripping_lava"
    """Dripping lava through blocks that haven't dripped down yet."""
    DRIPPING_OBSIDIAN_TEAR = "dripping_obsidian_tear"
    """Dripping crying obsidian's particles through blocks that haven't dripped down yet."""
    DRIPPING_WATER = "dripping_water"
    """Dripping water through blocks, wet sponges, leaves when raining that haven't dripped down yet."""
    DUST = "dust"
    """Redstone ore, powered redstone dust, redstone torches, powered redstone repeaters."""
    DUST_COLOR_TRANSITION = "dust_color_transition"
    """Sculk sensor gets triggered."""
    EFFECT = "effect"
    """Splash potions, lingering potions, bottles o' enchanting, evokers."""
    ELDER_GUARDIAN = "elder_guardian"
    """Elder guardians."""
    ELECTRIC_SPARK = "electric_spark"
    """Appears when a lightning bolt hits copper blocks."""
    ENCHANT = "enchant"
    """From bookshelves near an enchanting table."""
    ENCHANTED_HIT = "enchanted_hit"
    """Attacking with a sword or axe enchanted with Sharpness, Smite, or Bane of Arthropods."""
    END_ROD = "end_rod"
    """End rods, shulker bullets."""
    ENTITY_EFFECT = "entity_effect"
    """Status effects, lingering potions, tipped arrows, trading, withered armor (linger potion particles decrease when the "minimal" particle setting is used)."""
    EXPLOSION = "explosion"
    """Explosions, ghast fireballs, wither skulls, ender dragon death, shearing mooshrooms."""
    EXPLOSION_EMITTER = "explosion_emitter"
    """Explosions, ender dragon death."""
    FALLING_DRIPSTONE_LAVA = "falling_dripstone_lava"
    """Falling lava particles from the pointed dripstone."""
    FALLING_DRIPSTONE_WATER = "falling_dripstone_water"
    """Falling water particles from the pointed dripstone."""
    FALLING_DUST = "falling_dust"
    """Floating sand, gravel, concrete powder, and anvils."""
    FALLING_HONEY = "falling_honey"
    """Dripping honey through blocks that is dripping down in air."""
    FALLING_LAVA = "falling_lava"
    """Dripping lava through blocks that is dripping down in air."""
    FALLING_NECTAR = "falling_nectar"
    """Nectar on the pollen-loaded bees."""
    FALLING_OBSIDIAN_TEAR = "falling_obsidian_tear"
    """Dripping crying obsidian's particles through blocks that is dripping down in air and has fallen to the ground."""
    FALLING_SPORE_BLOSSOM = "falling_spore_blossom"
    """Dripping green particle from the spore blossom."""
    FALLING_WATER = "falling_water"
    """Dripping water through blocks that is dripping down in air and has fallen to the ground."""
    FIREWORK = "firework"
    """Firework rocket trail and explosion (trail is not shown when the "minimal" particle setting is used), when dolphins track shipwrecks and underwater ruins."""
    FISHING = "fishing"
    """Fishing."""
    FLAME = "flame"
    """Torches, furnaces, magma cubes, spawners."""
    FLASH = "flash"
    """Flash light when firework rocket explodes."""
    GLOW = "glow"
    """Glow squid."""
    GLOW_SQUID_INK = "glow_squid_ink"
    """Glow squid getting hurt."""
    HAPPY_VILLAGER = "happy_villager"
    """Applying bone meal to a crop, trading with villagers, feeding baby animals, walking or jumping on turtle eggs."""
    HEART = "heart"
    """Breeding and taming animals."""
    INSTANT_EFFECT = "instant_effect"
    """Instant health/damage splash and lingering potions, spectral arrows."""
    ITEM = "item"
    """Eating, thrown eggs, splash potions, eyes of ender, breaking tools."""
    ITEM_SLIME = "item_slime"
    """Jumping slimes."""
    ITEM_SNOWBALL = "item_snowball"
    """Thrown snowballs, creating withers, creating iron golems."""
    LANDING_HONEY = "landing_honey"
    """Dripping honey through blocks that has fallen to the ground."""
    LANDING_LAVA = "landing_lava"
    """Dripping lava through blocks that has fallen to the ground."""
    LANDING_OBSIDIAN_TEAR = "landing_obsidian_tear"
    """Dripping crying obsidian's particles through blocks that has fallen to the ground."""
    LARGE_SMOKE = "large_smoke"
    """Fire, minecart with furnace, blazes, water flowing into lava, lava flowing into water."""
    LAVA = "lava"
    """Lava bubble."""
    LIGHT = "light"
    """Light block displays it when the player holds the Light item of any level."""
    MYCELIUM = "mycelium"
    """Mycelium blocks."""
    NAUTILUS = "nautilus"
    """Activated conduits."""
    NOTE = "note"
    """Emitted from note blocks and jukeboxes."""
    POOF = "poof"
    """Explosions, death of mobs, mobs spawned from a spawner, silverfish infesting blocks."""
    PORTAL = "portal"
    """Nether portals, endermen, endermites, ender pearls, eyes of ender, ender chests, dragon eggs, teleporting from eating chorus fruits, end gateway portals."""
    RAIN = "rain"
    """Rain splashes on the ground."""
    SCRAPE = "scrape"
    """Scraping oxidation off a copper block with an axe."""
    SCULK_CHARGE = "sculk_charge"
    """Shown as sculk spreads through other blocks."""
    SCULK_CHARGE_POP = "sculk_charge_pop"
    """Sculk charge ends by popping."""
    SCULK_SOUL = "sculk_soul"
    """When a mob dies near a Sculk Catalyst these particles are shown."""
    SHRIEK = "shriek"
    """Shown when a Sculk Shrieker triggers."""
    SMOKE = "smoke"
    """Torches, primed TNT, droppers, dispensers, end portals, brewing stands, spawners, furnaces, ghast fireballs, wither skulls, taming, withers, lava (when raining), placing an eye of ender in an end portal frame, redstone torches burning out, food items on campfire."""
    SNEEZE = "sneeze"
    """Baby pandas sneezing."""
    SNOWFLAKE = "snowflake"
    """Appears when sinking in powder snow."""
    SOUL = "soul"
    """Appears when walking on Soul Sand or Soul Soil with the Soul Speed Enchantment, when a Mob dies near a Sculk Catalyst."""
    SOUL_FIRE_FLAME = "soul_fire_flame"
    """Appears on top of soul torches as a flame."""
    SPIT = "spit"
    """Llamas spitting at a player or mob."""
    SPORE_BLOSSOM_AIR = "spore_blossom_air"
    """Emits around a spore blossom."""
    SPLASH = "splash"
    """Entities in water, wolves shaking off after swimming, boats."""
    SQUID_INK = "squid_ink"
    """Produced by squid when attacked."""
    SWEEP_ATTACK = "sweep_attack"
    """A sword's sweep attack."""
    TOTEM_OF_UNDYING = "totem_of_undying"
    """Activated totem of undying."""
    UNDERWATER = "underwater"
    """Seen while underwater."""
    VIBRATION = "vibration"
    """Sculk sensor gets triggered."""
    WARPED_SPORE = "warped_spore"
    """A warped particle generated in warped forest biome environment."""
    WAX_OFF = "wax_off"
    """Appears when removing wax from a copper block."""
    WAX_ON = "wax_on"
    """Appears when waxing a copper block with honeycomb."""
    WHITE_ASH = "white_ash"
    """Naturally generated in basalt deltas biome environment."""
    WITCH = "witch"
    """Witches."""

    @staticmethod
    def display_name(elem) -> str:
        return {Particle.AMBIENT_ENTITY_EFFECT: "Ambient Entity Effect", Particle.ANGRY_VILLAGER: "Angry Villager",
                Particle.ASH: "Ash", Particle.BARRIER: "Barrier", Particle.BLOCK: "Block",
                Particle.BLOCK_MARKER: "Block Marker", Particle.BUBBLE: "Bubble",
                Particle.BUBBLE_COLUMN_UP: "Bubble Column Up", Particle.BUBBLE_POP: "Bubble Pop",
                Particle.CAMPFIRE_COSY_SMOKE: "Campfire Cosy Smoke",
                Particle.CAMPFIRE_SIGNAL_SMOKE: "Campfire Signal Smoke", Particle.CLOUD: "Cloud",
                Particle.COMPOSTER: "Composter", Particle.CRIMSON_SPORE: "Crimson Spore", Particle.CRIT: "Crit",
                Particle.CURRENT_DOWN: "Current Down", Particle.DAMAGE_INDICATOR: "Damage Indicator",
                Particle.DOLPHIN: "Dolphin", Particle.DRAGON_BREATH: "Dragon Breath",
                Particle.DRIPPING_DRIPSTONE_LAVA: "Dripping Dripstone Lava",
                Particle.DRIPPING_DRIPSTONE_WATER: "Dripping Dripstone Water",
                Particle.DRIPPING_HONEY: "Dripping Honey", Particle.DRIPPING_LAVA: "Dripping Lava",
                Particle.DRIPPING_OBSIDIAN_TEAR: "Dripping Obsidian Tear", Particle.DRIPPING_WATER: "Dripping Water",
                Particle.DUST: "Dust", Particle.DUST_COLOR_TRANSITION: "Dust Color Transition",
                Particle.EFFECT: "Effect", Particle.ELDER_GUARDIAN: "Elder Guardian",
                Particle.ELECTRIC_SPARK: "Electric Spark", Particle.ENCHANT: "Enchant",
                Particle.ENCHANTED_HIT: "Enchanted Hit", Particle.END_ROD: "End Rod",
                Particle.ENTITY_EFFECT: "Entity Effect", Particle.EXPLOSION: "Explosion",
                Particle.EXPLOSION_EMITTER: "Explosion Emitter",
                Particle.FALLING_DRIPSTONE_LAVA: "Falling Dripstone Lava",
                Particle.FALLING_DRIPSTONE_WATER: "Falling Dripstone Water", Particle.FALLING_DUST: "Falling Dust",
                Particle.FALLING_HONEY: "Falling Honey", Particle.FALLING_LAVA: "Falling Lava",
                Particle.FALLING_NECTAR: "Falling Nectar", Particle.FALLING_OBSIDIAN_TEAR: "Falling Obsidian Tear",
                Particle.FALLING_SPORE_BLOSSOM: "Falling Spore Blossom", Particle.FALLING_WATER: "Falling Water",
                Particle.FIREWORK: "Firework", Particle.FISHING: "Fishing", Particle.FLAME: "Flame",
                Particle.FLASH: "Flash", Particle.GLOW: "Glow", Particle.GLOW_SQUID_INK: "Glow Squid Ink",
                Particle.HAPPY_VILLAGER: "Happy Villager", Particle.HEART: "Heart",
                Particle.INSTANT_EFFECT: "Instant Effect", Particle.ITEM: "Item", Particle.ITEM_SLIME: "Item Slime",
                Particle.ITEM_SNOWBALL: "Item Snowball", Particle.LANDING_HONEY: "Landing Honey",
                Particle.LANDING_LAVA: "Landing Lava", Particle.LANDING_OBSIDIAN_TEAR: "Landing Obsidian Tear",
                Particle.LARGE_SMOKE: "Large Smoke", Particle.LAVA: "Lava", Particle.LIGHT: "Light",
                Particle.MYCELIUM: "Mycelium", Particle.NAUTILUS: "Nautilus", Particle.NOTE: "Note",
                Particle.POOF: "Poof", Particle.PORTAL: "Portal", Particle.RAIN: "Rain", Particle.SCRAPE: "Scrape",
                Particle.SCULK_CHARGE: "Sculk Charge", Particle.SCULK_CHARGE_POP: "Sculk Charge Pop",
                Particle.SCULK_SOUL: "Sculk Soul", Particle.SHRIEK: "Shriek", Particle.SMOKE: "Smoke",
                Particle.SNEEZE: "Sneeze", Particle.SNOWFLAKE: "Snowflake", Particle.SOUL: "Soul",
                Particle.SOUL_FIRE_FLAME: "Soul Fire Flame", Particle.SPIT: "Spit",
                Particle.SPORE_BLOSSOM_AIR: "Spore Blossom Air", Particle.SPLASH: "Splash",
                Particle.SQUID_INK: "Squid Ink", Particle.SWEEP_ATTACK: "Sweep Attack",
                Particle.TOTEM_OF_UNDYING: "Totem Of Undying", Particle.UNDERWATER: "Underwater",
                Particle.VIBRATION: "Vibration", Particle.WARPED_SPORE: "Warped Spore", Particle.WAX_OFF: "Wax Off",
                Particle.WAX_ON: "Wax On", Particle.WHITE_ASH: "White Ash", Particle.WITCH: "Witch"}[elem]
