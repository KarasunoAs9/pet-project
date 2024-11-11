

document.querySelectorAll('select[name="quantity"]').forEach(select => {
    select.addEventListener('change', function() {
        const cartId = this.closest('.cart-item').querySelector('input[name="cart_id"]').value;
        const quantity = this.value;

        fetch("{% url 'update-cart' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({ cart_id: cartId, quantity: quantity })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.querySelector('.cart-total h2').innerText = `Total: $${data.total_sum}`;
            } else {
                alert(data.error || "Error updating cart.");
            }
        })
        .catch(error => console.error("Error:", error));
    });
});
