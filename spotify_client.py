"""
Spotify client abstraction layer
Currently uses mock data, designed to easily swap to real Spotify API
"""

from mock_data import ARTISTS, RELATED_ARTISTS


class SpotifyClient:
    """
    Handles all Spotify data operations.
    Currently returns mock data. Later: implement real Spotify Web API calls.
    """

    def __init__(self):
        # TODO: When ready for real API, initialize with credentials:
        # self.client_id = client_id
        # self.client_secret = client_secret
        # self.sp = spotipy.Spotify(auth_manager=...)
        pass

    def search_artist(self, artist_name):
        """
        Search for an artist by name.

        Args:
            artist_name: Name of the artist to search for

        Returns:
            Artist dict if found, None otherwise

        TODO: Replace with real Spotify API call:
        results = self.sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
        if results['artists']['items']:
            return results['artists']['items'][0]
        """
        artist_name_lower = artist_name.lower().replace(" ", "_")

        # Simple fuzzy matching on mock data
        for key, artist in ARTISTS.items():
            if artist_name_lower in key or artist_name_lower in artist['name'].lower():
                return artist

        return None

    def get_related_artists(self, artist_id):
        """
        Get artists related to the given artist.

        Args:
            artist_id: Spotify artist ID

        Returns:
            List of related artist dicts

        TODO: Replace with real Spotify API call:
        results = self.sp.artist_related_artists(artist_id)
        return results['artists']
        """
        # Find the artist key by ID
        artist_key = None
        for key, artist in ARTISTS.items():
            if artist['id'] == artist_id:
                artist_key = key
                break

        if not artist_key or artist_key not in RELATED_ARTISTS:
            return []

        # Get related artist keys and return full artist objects
        related_keys = RELATED_ARTISTS[artist_key]
        return [ARTISTS[key] for key in related_keys if key in ARTISTS]

    def get_artist_details(self, artist_id):
        """
        Get detailed information about an artist.

        Args:
            artist_id: Spotify artist ID

        Returns:
            Artist dict if found, None otherwise

        TODO: Replace with real Spotify API call:
        return self.sp.artist(artist_id)
        """
        for artist in ARTISTS.values():
            if artist['id'] == artist_id:
                return artist

        return None
