function sendMail(contactForm) {
    emailjs.send("gmail", "gm_classes", {
        "your_name": contactForm.id_your_name.value,
        "your_email": contactForm.id_your_email.value,
        "your_request": contactForm.id_your_request.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}

