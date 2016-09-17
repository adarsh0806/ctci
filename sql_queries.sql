-- Table structure

-- movie	actor	casting

-- id	      id	movieid
-- title	name	actorid
-- yr		        ord
-- director		
-- budget		
-- gross		


-- List the film title and the leading actor for all of the films 'Julie Andrews' played in.
SELECT title, name
  FROM movie, casting, actor
  WHERE movieid=movie.id
    AND actorid=actor.id
    AND ord=1
    AND movieid IN
    (SELECT movieid FROM casting, actor
     WHERE actorid=actor.id
     AND name='Julie Andrews')

-- Obtain a list, in alphabetical order, of actors who've had at least 30 starring roles.
SELECT name
    FROM casting JOIN actor
      ON  actorid = actor.id
    WHERE ord=1
    GROUP BY name
    HAVING COUNT(movieid)>=30

-- List the films released in the year 1978 ordered by the number of actors in the cast.
Select title, count(*) as 'number_of_actors'
From movie Join casting
On id = movieid
Where yr = '1978'
Group by title
Order by COUNT(actorid) desc

-- List all the people who have worked with 'Art Garfunkel'.

Select name
From actor Join casting
On id = actorid
Where movieid in
(Select movieid
From casting Join actor
On id = actorid
Where name = 'Art Garfunkel')
And name != 'Art Garfunkel'
Order by name