const links = document.querySelectorAll('.nav-link')

let active_link = null

links.forEach((link) => {
    link.addEventListener('click', (e) => {
        // e.preventDefault()
        
        if (active_link) {
            active_link.classList.remove('focus')
        }
        link.classList.add('focus');
        active_link = link
    })
});