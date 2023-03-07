# This program takes a film description and compares it against each film description from the txt file.
# A for loop is used to conduct word vector similarity between each film description and the description from Planet Hulk.
# For each description, if the similarity score is higher than that of the previous score, the film description is stored.
# The similar movie function prints out the film description and associated movie title which had the highest word vector similarity.
import spacy


def similar_movie(main_description):
    similarity_score = 0
    recommendation = ""
    for count, description in enumerate(movie_descriptions):
        similarity = nlp(description).similarity(main_description)
        if similarity > similarity_score:
            similarity_score = similarity
            recommendation = description
            title = movie_titles[count]
    print(f"Recommended Movie: {title}\nDescription:\n{recommendation}")


nlp = spacy.load('en_core_web_md')
description_to_compare = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planat Sakaar where he is sold into slavery and trained as a gladiator")
movie_titles = []
movie_descriptions = []
main_description = nlp(description_to_compare)

# Reading and saving movie information to lists.
with open("movies.txt", "r") as file:
    data = file.readlines()
    for line in data:
        split_movie = line.split(" :")
        movie_descriptions.append(split_movie[1])
        movie_titles.append(split_movie[0])

similar_movie(main_description)
