import pandas as pd


class Main:
    """
    A Python Class that uses IMDB data from the top 1,000 movies from 2006 to
    2016. The Class uses movies to actively narrow down suggestions for users,
    based off user input.
    """
    def __init__(self,data,data2):
        self.data = data
        self.data2 = data2
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 200)
        pd.set_option('display.max_colwidth', -1)

    def call_functions(self):
        """
        A python class method that requires user input based off of what they
        would like to do in our program. Depending on what the user wants to
        search, this method directs to the method of their choosing.

        Returns: Runs another method within the class based off of user input.

        """
        x = input('Welcome to our movie recommender! Please enter either: '
                  'Actor, Director, Genre, Top 10, or Recommendation to '
                  'apply filters ')
        if x == 'Actor':
            self.actor_movies()
        if x == 'Director':
            self.director_movies()
        if x == 'Genre':
            self.genres()
        if x == 'Top 10':
            self.suggestion()
        if x == 'Recommendation':
            self.recommendation()

    def actor_movies(self):
        """
        A python class method that takes in user input for the users favorite
        actor, then shows a list of the movies with that actor. It then asks the
        user if he would like to narrow his search preferences down based off of
        genre, director, both, or neither. Depending on what the user decides,
        it chooses the right way to narrow the search results. It then allows
        users to view more information about a specific film, or change their
        original search entries redirecting them back to the call_functions
        method.

        Returns: A list of the user preferred movies based off of their search
        inquiries.

        """
        a = input('Please enter your favorite actor ')
        data1 = self.data[data.Actors.str.contains(a)]
        print(self.data[data.Actors.str.contains(a)])
        x = input('What other things would you like to see in your movie? '
                  'Please enter a Genre, Director, Both, or None ')
        if x == 'Genre':
            y = input('Enter your desired Genre: ')
            print(data1[data.Genre.str.contains(y)])

        elif x == 'Director':
            z = input('Enter your desired Director: ')
            print(data1.loc[data['Director'] == z])

        elif x == 'Both':
            u = input('enter your desired genre')
            w = input('enter your desired director')
            new_1 = pd.DataFrame()
            data2 = data1[data.Genre.str.contains(u)]
            new_1 = new_1.append(data2.loc[data['Director'] == w])
            print(new_1)

        elif x == 'None':
            x = (input('Would you like to view more about one of these films?'
                       ' Y/N '))
            if x == 'Y':
                self.info()
            elif x == 'N':
                retry = input('Would you like to change your search entries?'
                              ' Y/N ')
                if retry == 'Y':
                    self.call_functions()
                elif retry == 'N':
                    print('Okay enjoy your movie!')

    def director_movies(self):
        """
        A python class method that takes in user input for the users favorite
        director, then shows a list of the movies with that director. It then
        asks if the user would like to narrow their results based off Genre, if
        no it asks the users if they want to change their original search
        entries redirecting them back to the call_functions method.

        Returns: A list of user preferred movies based off of favorite director,
        and possibly genre.

        """
        director = input('Please enter your favorite director: ')
        print(self.data.loc[data['Director'] == director])
        data_direct = self.data.loc[data['Director'] == director]
        i = input('Would you like to view their movies by a specific genre? ')
        if i == 'Y':
            ask = input('What Genre? ')
            print(data_direct[data.Genre.str.contains(ask)])
            x = (input('Would you like to view more about one of these films?'
                       ' Y/N '))
            if x == 'Y':
                self.info()
            elif x == 'N':
                retry = input('Would you like to change your search entries?'
                              ' Y/N ')
                if retry == 'Y':
                    self.call_functions()
                elif retry == 'N':
                    print('Okay enjoy your movie!')
        elif i == 'N':
            retry = input('Would you like to change your search entries?'
                          ' Y/N ')
            if retry == 'Y':
                self.call_functions()
            elif retry == 'N':
                print('Okay enjoy your movie!')

    def genres(self):
        """
        A python class method that takes in user input for the users favorite
        genre, then shows a list of the movies with that genre. It then asks the
        user if he would like to narrow his search preferences down based off of
        actor. Depending on what the user decides, it either narrows down, or
        asks the user if they would like to change their original search entries
        redirecting them back to the call_functions method.

        Returns: A list of user preferred movies based off genre, then possibly
        a more narrow list of movies from a user input actor that has movies in
        that genre.

        """
        genre = input('Please enter your favorite genre: ')
        print(self.data[data.Genre.str.contains(genre)])
        data_genre = self.data[data.Genre.str.contains(genre)]
        actor_data = input('Would you like to search for a specific actor?')
        if actor_data == 'Y':
            ask = input('What Actor? ')
            print(data_genre[data.Actors.str.contains(ask)])
            x = (input('Would you like to view more about one of these films?'
                       ' Y/N '))
            if x == 'Y':
                self.info()
            elif x == 'N':
                retry = input('Would you like to change your search entries?'
                              ' Y/N ')
                if retry == 'Y':
                    self.call_functions()
                elif retry == 'N':
                    print('Okay enjoy your movie!')

        if actor_data == 'N':
            retry = input('Would you like to change your search entries?'
                          ' Y/N ')
            if retry == 'Y':
                self.call_functions()
            elif retry == 'N':
                print('Okay enjoy your movie!')

    def recommendation(self):
        """
        A python class method that takes in user input for the users favorite
        actor, favorite director, favorite genre, preferred rating. The program
        then returns a list of movies from your actor, your director, and that
        genre. It then allows you to view more information about one of the
        movies we suggested, and if not it allows you to change original search
        entries.

        Returns: A list of movies based off the user specified preferences.

        """
        actor = input('Please enter your favorite Actor: ')
        director = input('Please enter your favorite Director: ')
        genre = input('Please enter your favorite Genre: ')
        new = pd.DataFrame()
        new = new.append(self.data[data.Actors.str.contains(actor)])
        new = new.append(self.data.loc[data['Director'] == director])
        new = new.append(self.data[data.Genre.str.contains(genre)])
        new = new.drop_duplicates()
        print(new[data.Rating >= float(input('Please enter the lowest '
                                             'acceptable rating for a '
                                             'movie '))])

        x = (input('Would you like to view more about one of these films?'
                   ' Y/N '))
        if x == 'Y':
            self.info()
        elif x == 'N':
            retry = input('Would you like to change your search entries?'
                          ' Y/N ')
            if retry == 'Y':
                self.call_functions()
            elif retry == 'N':
                print('Okay enjoy your movie!')

    def suggestion(self):
        """
        A python class method that is used to present the Top 10 movies on IMDB
        from 2006-2016. The program ranks the movies based off of ratign and
        allows the user to view more information about each individual film. If
        they choose not to, they can change their original search entries.

        Returns: A list of the Top 10 movies, and then descriptions of a
        specific user preferred movie.

        """
        ratings = self.data.groupby('Title')['Rating'].mean() \
            .sort_values(ascending=False)
        print('Here are the top 10 movies on IMDB with their ratings: '
              , ratings.head(10))
        y = input('Would you like to view more about one of these films? Y/N ')
        if y == 'Y':
            self.info()
        if y == 'N':
            retry = input('Would you like to change your search entries?'
                          ' Y/N ')
            if retry == 'Y':
                self.call_functions()
            elif retry == 'N':
                print('Okay enjoy your movie!')

    def info(self):
        """
        A python class method that allows the user to view more information
        about a film of their choosing throughout our class. It allows users to
        enter in the title of the film and it returns the description and year
        that the movie was produced.
        Returns: A description and year of the user specified movie.

        """
        more = input('What film would you like to view? ')
        print(self.data2.loc[data['Title'] == more])
        y = input('Would you like to view another? ')
        if y == 'Y':
            self.info()
        if y == 'N':
            retry = input('Would you like to change your search entries?'
                          ' Y/N ')
            if retry == 'Y':
                self.call_functions()
            elif retry == 'N':
                print('Okay enjoy your movie!')


if __name__ == "__main__":
    data = pd.read_csv('Final.csv')
    data2 = pd.read_csv('New .csv')
    self = Main(data,data2)
    self.call_functions()