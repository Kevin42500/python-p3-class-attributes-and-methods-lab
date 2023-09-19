import pytest
from song import Song

class TestSong:
    @classmethod
    def setup_class(cls):
        # Create sample songs only once, before all tests
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    def test_saves_name_artist_genre(self):
        # Create a new song for this specific test
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert out_of_touch.name == "Out of Touch"
        assert out_of_touch.artist == "Hall and Oates"
        assert out_of_touch.genre == "Pop"

    def test_has_song_count(self):
        # Create new songs for this specific test
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.count == 4  # 3 sample songs + 1 created in this test

    def test_has_genres(self):
        assert "Rap" in Song.genres
        assert "Pop" in Song.genres
        assert "Rock" in Song.genres

    def test_has_artists(self):
        assert "Jay-Z" in Song.artists
        assert "Beyonce" in Song.artists
        assert "Hall and Oates" in Song.artists

    def test_has_genre_count(self):
        # Create new songs for this specific test
        Song("Another Rap Song", "Eminem", "Rap")
        assert Song.genre_count["Rap"] == 2  # 1 from the sample songs + 1 created in this test

    def test_has_artist_count(self):
        # Create new songs for this specific test
        Song("Another Jay-Z Song", "Jay-Z", "Rap")
        assert Song.artist_count["Jay-Z"] == 2  # 1 from the sample songs + 1 created in this test

if __name__ == '__main__':
    pytest.main()
