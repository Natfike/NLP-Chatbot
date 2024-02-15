$(document).ready(function() {
    $("#myForm").submit(function(event) {
        event.preventDefault(); // Empêcher le formulaire d'être soumis normalement

        // Récupérer la valeur de l'input
        var inputValue = $("#input").val();

        // Créer un objet JSON avec la valeur de l'input
        var jsonData = { input: inputValue };

        // Convertir l'objet JSON en chaîne JSON
        var jsonString = JSON.stringify(jsonData);

        // Envoyer les données JSON à l'adresse spécifiée
        $.ajax({
            url: "http://localhost:5010/askBOWChatbot",
            type: "POST",
            contentType: "application/json",
            data: jsonString,
            success: function(data) {
                console.log("Réponse du serveur:", data);
            },
            error: function(xhr, status, error) {
                console.error("Erreur:", error);
            }
        });
    });
});
