#!/usr/bin/env python3
"""
Music Artist Discovery Tool
Discovers new artists based on similarity to a seed artist
"""

import sys
from spotify_client import SpotifyClient


def discover_artists(seed_artist_name, max_followers=500000, limit=10):
    """
    Discover new artists similar to the seed artist.

    Args:
        seed_artist_name: Name of the artist to base discovery on
        max_followers: Maximum followers for "undiscovered" artists
        limit: Maximum number of artists to return

    Returns:
        List of discovered artist dicts
    """
    client = SpotifyClient()

    # Search for the seed artist
    print(f"🔍 Searching for '{seed_artist_name}'...")
    seed_artist = client.search_artist(seed_artist_name)

    if not seed_artist:
        print(f"❌ Could not find artist: {seed_artist_name}")
        return []

    print(f"✓ Found: {seed_artist['name']} ({seed_artist['followers']:,} followers)\n")

    # Get related artists
    print("🎵 Finding related artists...")
    related_artists = client.get_related_artists(seed_artist['id'])

    if not related_artists:
        print("❌ No related artists found")
        return []

    print(f"✓ Found {len(related_artists)} related artists\n")

    # Filter for "undiscovered" artists (low follower count)
    print(f"🔎 Filtering for artists with < {max_followers:,} followers...")
    discovered = []

    for artist in related_artists:
        if artist['followers'] < max_followers:
            # Simple discovery score: lower followers = more "undiscovered"
            discovery_score = 100 - (artist['followers'] / max_followers * 100)
            artist['discovery_score'] = round(discovery_score, 1)
            discovered.append(artist)

    # Sort by discovery score (highest first)
    discovered.sort(key=lambda a: a['discovery_score'], reverse=True)

    return discovered[:limit]


def print_results(artists):
    """Pretty print discovered artists."""
    if not artists:
        print("\n😕 No undiscovered artists found. Try increasing max_followers threshold.")
        return

    print(f"\n✨ Discovered {len(artists)} artists:\n")
    print("-" * 80)

    for i, artist in enumerate(artists, 1):
        genres = ", ".join(artist['genres'][:3])  # Show first 3 genres
        print(f"{i}. {artist['name']}")
        print(f"   Followers: {artist['followers']:,}")
        print(f"   Genres: {genres}")
        print(f"   Discovery Score: {artist['discovery_score']}/100")
        print(f"   Popularity: {artist['popularity']}/100")
        print()


def main():
    """Main entry point."""
    # Get seed artist from command line or prompt
    if len(sys.argv) > 1:
        seed_artist = " ".join(sys.argv[1:])
    else:
        seed_artist = input("Enter an artist name: ").strip()

    if not seed_artist:
        print("Please provide an artist name")
        sys.exit(1)

    # Discover artists
    discovered = discover_artists(
        seed_artist_name=seed_artist,
        max_followers=500000,  # Artists with < 500k followers
        limit=10
    )

    # Print results
    print_results(discovered)


if __name__ == "__main__":
    main()
