document.addEventListener('DOMContentLoaded', () => {
	const hello = document.querySelector('#hello');

	const run = async () => {
		const req = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
		const res = await req.json();

		hello.textContent = res.hello;
	};

	run();
});
