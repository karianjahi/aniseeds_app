import random

MOVIES_LIST = ["Lord of the Rings",
                "Pulp Fiction",
                "Big Fish",
                "Blade Runner",
                "Melancholia",
                "Metropolis",
                "Shawshank Redemption",
                "Spirited Away",
                "Dr. Strangelove",
                "WALL-E",
                "The Lives of Others",
                "2001: A Space Odyssey",
                "La Dolce Vita",
                "Citizen Kane",
                "Gone with the Wind",
                "Die Hard"]

def random_recommender():
    """chooses 3 random movies without replacement"""
    return random.sample(MOVIES_LIST, 3)

def random_recommender2(ratings_dict):
# {movie:rating, movie:rating}
    pass

def nmf_recommender():
    pass

def cosine_recommender():
    pass

if __name__ == '__main__':
    print(f"Your recommendations are:\n{', '.join(random_recommender())}")
