describe('Prueba crear cuenta e2e', function() {
    it('Crea cuenta CI-Chile', function() {
      cy.visit('http://127.0.0.1:8000/');
      cy.contains('empresa').click()
      cy.visit('http://127.0.0.1:8000/account/signin/')
      cy.contains('Sign in').click()
      cy.get('input#id_username').type('cichile')
      cy.get('input#id_password').type('cichile')
      cy.contains('Sign in').click()
      cy.visit('http://127.0.0.1:8000/category/motor')
      
  })
})