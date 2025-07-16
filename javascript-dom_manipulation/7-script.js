const ul = document.querySelector('#list_movies');

const run = async () => {
	const req = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
	const res = await req.json();

	res.results.forEach((movie) => {
		const li = document.createElement('li');
		li.textContent = movie.title;

		ul.append(li);
	});
};

run();
