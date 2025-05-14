import pytest
from app.provider_check import provider_is_valid

class TestProviderCheck():

    #
    # Positive testing
    #

    # Valid equivalence partition: 15-50
    @pytest.mark.parametrize('experience_years', [
        (15),   # Valid lower boundary
        (16),
        (27),
        (49),
        (50),   # Valid upper boundary
    ])
    def test_provider_check_passes(self, experience_years):
        assert provider_is_valid(experience_years)

    #
    # Negative testing
    #

    # Invalid equivalence partitions: 0-14 and 51-MAX INTEGER
    @pytest.mark.parametrize('experience_years', [
        (0),
        (1),
        (7),
        (13),
        (14),   # Invalid lower boundary
        (51),   # Invalid upper boundary
        (52),
        (65)
    ])
    def test_provider_check_fails(self, experience_years):
        assert not provider_is_valid(experience_years)