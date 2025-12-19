"""
Mock Spotify artist data
Structure mirrors Spotify Web API response format
"""

ARTISTS = {
    "radiohead": {
        "id": "4Z8W4fKeB5YxbusRsdQVPb",
        "name": "Radiohead",
        "genres": ["alternative rock", "art rock", "melancholia", "permanent wave", "rock"],
        "followers": 6789234,
        "popularity": 82,
    },
    "thom_yorke": {
        "id": "3WrFJ7ztbogyGnTHbHJFl2",
        "name": "Thom Yorke",
        "genres": ["alternative rock", "art rock", "electronica"],
        "followers": 892456,
        "popularity": 68,
    },
    "atoms_for_peace": {
        "id": "4qrHIKHWsJ7fVM557t1TaW",
        "name": "Atoms for Peace",
        "genres": ["alternative rock", "art rock", "experimental"],
        "followers": 234567,
        "popularity": 58,
    },
    "portishead": {
        "id": "6Qh2VcFJUqTMshLSMqWl8T",
        "name": "Portishead",
        "genres": ["trip hop", "electronic", "art pop"],
        "followers": 1234567,
        "popularity": 72,
    },
    "massive_attack": {
        "id": "6FXMGKc8QfMssLiyxLfyvQ",
        "name": "Massive Attack",
        "genres": ["trip hop", "electronic", "downtempo"],
        "followers": 2345678,
        "popularity": 75,
    },
    "sigur_ros": {
        "id": "6UUrUCIZtQeOf8pGOd1k9Y",
        "name": "Sigur Rós",
        "genres": ["icelandic post-rock", "dream pop", "ambient"],
        "followers": 1456789,
        "popularity": 70,
    },
    "jonsi": {
        "id": "1xU878Z1QtBldR7ru9owdU",
        "name": "Jónsi",
        "genres": ["icelandic indie", "art pop"],
        "followers": 187654,
        "popularity": 55,
    },
    "godspeed": {
        "id": "4svpOyfmQKuWpHLjgy4cdK",
        "name": "Godspeed You! Black Emperor",
        "genres": ["post-rock", "experimental", "drone"],
        "followers": 345678,
        "popularity": 62,
    },
    "mogwai": {
        "id": "34UhPkLbtFKRq3nmfFgejG",
        "name": "Mogwai",
        "genres": ["post-rock", "scottish indie"],
        "followers": 567890,
        "popularity": 65,
    },
    "explosions": {
        "id": "4V3dFPPG8N9DqOlKqBWCWq",
        "name": "Explosions in the Sky",
        "genres": ["post-rock", "instrumental rock"],
        "followers": 789012,
        "popularity": 67,
    },
    "tortoise": {
        "id": "0V9xjZwKXzeWZjqSGMZwGc",
        "name": "Tortoise",
        "genres": ["post-rock", "chicago indie", "math rock"],
        "followers": 123456,
        "popularity": 52,
    },
    "gy_be": {
        "id": "7lQ4kC9SRgXdUs1CUw4r1R",
        "name": "GY!BE",
        "genres": ["post-rock", "experimental"],
        "followers": 89012,
        "popularity": 48,
    },
    "silver_mt_zion": {
        "id": "2mVVjNCXMBPDFMGLBUwNDq",
        "name": "Thee Silver Mt. Zion Memorial Orchestra",
        "genres": ["post-rock", "experimental", "chamber pop"],
        "followers": 45678,
        "popularity": 42,
    },
    "talk_talk": {
        "id": "1dNdXfkjV4lP8wCqIjfbJr",
        "name": "Talk Talk",
        "genres": ["art rock", "post-rock", "new wave"],
        "followers": 678901,
        "popularity": 66,
    },
    "bark_psychosis": {
        "id": "8hK3fPNlEjqJzGFqQxdWHw",
        "name": "Bark Psychosis",
        "genres": ["post-rock", "experimental"],
        "followers": 34567,
        "popularity": 38,
    },
}

# Related artist mappings (artist_key -> list of related artist_keys)
RELATED_ARTISTS = {
    "radiohead": ["thom_yorke", "atoms_for_peace", "portishead", "massive_attack", "sigur_ros", "talk_talk"],
    "thom_yorke": ["radiohead", "atoms_for_peace", "portishead", "jonsi"],
    "atoms_for_peace": ["radiohead", "thom_yorke", "massive_attack"],
    "portishead": ["radiohead", "massive_attack", "talk_talk"],
    "massive_attack": ["portishead", "radiohead", "atoms_for_peace"],
    "sigur_ros": ["jonsi", "radiohead", "godspeed", "mogwai", "explosions"],
    "jonsi": ["sigur_ros", "radiohead", "thom_yorke"],
    "godspeed": ["sigur_ros", "mogwai", "silver_mt_zion", "gy_be", "tortoise"],
    "mogwai": ["godspeed", "explosions", "sigur_ros", "tortoise"],
    "explosions": ["mogwai", "godspeed", "sigur_ros", "tortoise"],
    "tortoise": ["mogwai", "godspeed", "explosions", "gy_be", "bark_psychosis"],
    "gy_be": ["godspeed", "silver_mt_zion", "tortoise"],
    "silver_mt_zion": ["godspeed", "gy_be", "tortoise"],
    "talk_talk": ["radiohead", "portishead", "bark_psychosis"],
    "bark_psychosis": ["talk_talk", "tortoise", "godspeed"],
}
