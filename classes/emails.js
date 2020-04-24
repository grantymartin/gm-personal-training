function sendMail(contactForm) {
    email.js.send("gmail", "gm-classes", {
        "your_name": email.your_name.value,
        "your_email": email.your_email.value,
        "your_request": email.your_request.value,
    })
}
