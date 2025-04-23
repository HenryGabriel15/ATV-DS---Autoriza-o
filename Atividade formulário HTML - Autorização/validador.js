function validarFormulario() {
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const senhaRegex = /^(?=.*[A-Z])(?=.*\d).{8,}$/;
  
    if (nome.length < 3) {
      alert("Nome deve ter pelo menos 3 caracteres.");
      return false;
    }
  
    if (!emailRegex.test(email)) {
      alert("E-mail inválido.");
      return false;
    }
  
    if (!senhaRegex.test(senha)) {
      alert("Senha deve ter pelo menos 8 caracteres, uma letra maiúscula e um número.");
      return false;
    }
  
    return true;
  }