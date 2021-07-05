# task 1 
def favourite_movie(movie):
    print("My favourite movie is:" +  movie)


favourite_movie("Beach") 
favourite_movie("whatewer") 
favourite_movie("oops") 
favourite_movie("somethin") 


#task 2
def make_country(country_name, capital):

 make_country("Sweden", "Stockholm")
 make_country("Poland", "Warsaw")
 make_country("Spain", "Madrid")


# task 3

def make_operation(operator, *numbers):
    print(operator.join(map(lambda a: str(a), numbers)))
    print(eval(operator.join(map(lambda a: str(a), numbers))))
make_operation('+', 7, 7, 2)  
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)
