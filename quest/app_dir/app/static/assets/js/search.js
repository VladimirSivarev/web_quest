function nextPage() {
	var value = document.getElementsByTagName("input")[0].value;
	document.getElementById("check").href = MD5(value);
}

document.getElementById("check").onclick = nextPage;
