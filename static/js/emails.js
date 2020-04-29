function sendMail(contactForm) {
    emailjs.send("gmail", "gm_classes", {
            "your_name": contactForm.id_your_name.value,
            "your_email": contactForm.id_your_email.value,
            "your_request": contactForm.id_your_request.value,
        })
        .then(
            function(response) {
                alert("Your message has been sent! GM-Personal-training will get back to you as soon as possible");
            },
            function(error) {
                alert("Sorry something has gone wrong here. We will aim to sort this problem as quickly as possible");
            }
        );
    return false; // To block from loading a new page
}
