from tmdbwrapper import TV
from pytest import fixture
import vcr


@fixture
def tv_keys():
    return['id', 'origin_country', 'poster_path', 'name' , 'overview', 'popularity', 'backdrop_path', 'first_air_date', 'vote_count' , 'vote_average']

@vcr.use_cassette ('tests/vcr_cassettes/tv-info.yml')
def test_tv_info():
    """""Tests an API call to get a TV show info"""
    tv_instance=TV(1396)
    response=tv_instance.info()
    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
    assert set(tv_keys()).issubset(response.keys())

@vcr.use_cassette('tests/vcr:cassetted/tv-popular.yml')
def test_tv_popular():
    """"tests an API call to get a popular tv shows"""

    response = TV.popular()
    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys()).issubset(response['results'][0].keys())


