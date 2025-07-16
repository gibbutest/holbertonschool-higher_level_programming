const run = async () => {
	const req = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
	const res = await req.json();

	document.querySelector('#character').textContent = res.name;
};

run();
