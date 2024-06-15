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


const phoneField = document.getElementById('phone');
const donateBtn = document.getElementById('donate-btn');

donateBtn.onclick = phoneField.blur();

phoneField.addEventListener('blur', function(e){
    const phoneNumber = phoneField.value;
    // phoneNumber = phoneNumber.toString()
    let phoneNumFormat = '';
    if (phoneNumber.startsWith('0')) {
        phoneNumFormat = '+233' + phoneNumber.replace(/^0/, '');
    } else {
        phoneNumFormat = phoneNumber
    }
    phoneField.value = phoneNumFormat;
});