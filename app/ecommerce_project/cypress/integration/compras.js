describe('Prueba comprar producto e2e', function() {
    it('Compra productos CI-Chile', function() {
      cy.visit('http://127.0.0.1:8000/gallery')
      cy.visit('http://127.0.0.1:8000/cart/add/8')
      cy.visit('http://127.0.0.1:8000/cart/add/5')
      cy.visit('http://127.0.0.1:8000/cart/add/7')
      cy.get('button[type="submit"] > span').click()
    })
  })