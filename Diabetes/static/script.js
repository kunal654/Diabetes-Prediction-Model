document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("predictionForm");
    
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        let isValid = true;

        // List of required fields
        const requiredFields = ["pregnancies", "glucose", "bloodPressure", "skinThickness", "insulin", "bmi", "dpf", "age"];
        
        // Check all fields for validity
        requiredFields.forEach(function(fieldId) {
            const field = document.getElementById(fieldId);
            if (!field.value) {
                isValid = false;
                field.style.borderColor = "red";
            } else {
                field.style.borderColor = "";
            }
        });

        if (!isValid) {
            alert("Please fill out all fields correctly.");
            return; // Exit the function if validation fails
        }

        // If the form is valid, you can proceed with form submission or an AJAX call
        const formData = new FormData(form);
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            // Update the page with the result
            const resultElement = document.getElementById('result');
            resultElement.innerHTML = `<p>${result.result}</p>`; // Display the result in the 'result' paragraph
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
