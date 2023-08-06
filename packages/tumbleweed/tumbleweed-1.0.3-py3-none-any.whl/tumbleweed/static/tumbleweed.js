const content_nodes = document.getElementsByClassName('dropdown');

for (let node of content_nodes) {
    const content = node.getElementsByTagName('content')[0];
    node.addEventListener('click', () => {
        if (content.style.display == 'block') {
            content.style.display = 'none';
        } else {
            content.style.display = 'block';
        }
    }) 
}
