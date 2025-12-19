# Music Artist Discovery

A simple prototype that discovers new music artists using basic signals.

## Quick Start

No dependencies needed (for now). Just run:

```bash
python discover.py "Radiohead"
```

Or without arguments to be prompted:

```bash
python discover.py
```

## How It Works

1. Searches for your seed artist
2. Finds related/similar artists
3. Filters for "undiscovered" artists (< 500k followers)
4. Ranks by discovery score (lower followers = higher score)
5. Returns top 10 results

## Example Output

```
🔍 Searching for 'Radiohead'...
✓ Found: Radiohead (6,789,234 followers)

🎵 Finding related artists...
✓ Found 6 related artists

🔎 Filtering for artists with < 500,000 followers...

✨ Discovered 3 artists:

--------------------------------------------------------------------------------
1. Thee Silver Mt. Zion Memorial Orchestra
   Followers: 45,678
   Genres: post-rock, experimental, chamber pop
   Discovery Score: 90.9/100
   Popularity: 42/100

2. Bark Psychosis
   Followers: 34,567
   Genres: post-rock, experimental
   Discovery Score: 93.1/100
   Popularity: 38/100
...
```

## Current Status

**✅ Working with mock data**
- Mock Spotify-like artist database
- ~15 artists with realistic metadata
- Related artist relationships

**🔜 Next steps**
- Swap mock data for real Spotify Web API
- Add virtual environment setup
- Add more discovery signals (genre matching, release recency, etc.)

## Architecture

```
discover.py          # Main script - discovery logic
spotify_client.py    # Data layer (easy to swap mock → real API)
mock_data.py         # Mock artist database
```

## When Ready for Real Spotify API

1. Create Spotify Developer account
2. Get Client ID + Secret
3. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install spotipy
   ```
4. Update `spotify_client.py` - replace mock functions with real API calls (TODOs are marked)
5. Add config file for credentials

All the hard-coded mock lookups will be replaced with simple spotipy calls.
