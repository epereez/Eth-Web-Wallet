document.getElementById("transactionform").addEventListener("submit",function(e){
    e.preventDefault();
    
    const address = document.getElementById("address")
    const amount = document.getElementById("amount")

    fetch("/api/transact", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({address: address},{amount: amount})
    })
    .then(response => response.json())
    .then(data => { 
        console.log("Success: ", data)
        document.getElementById("response").textContent = data.response
    })
    .catch((error) => {
        console.error("Error", error)
    })
})