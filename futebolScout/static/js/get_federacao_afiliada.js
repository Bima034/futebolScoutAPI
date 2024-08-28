document.addEventListener('DOMContentLoaded', function() {
    function fetchAfiliada(){
        const pais = document.getElementById('id_localidade').value;
        const currentUrl = window.location.href;
        const idMatch = currentUrl.match(/\/(\d+)$/);
        var id = idMatch ? idMatch[1] : null;
        if (!id) {
            id = 0;
        }
        // Supondo que `pais` e `id` estejam corretamente definidos no escopo
        fetch(`/federacao/get_lista_possiveis_afiliadas/${pais}/${id}`)
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
          })
          .then(data => {
            const selectElement = document.getElementById('id_afiliada');

            // Obtém o valor selecionado
            const selectedValue = selectElement.value;

            // Obtém o texto do item selecionado
            const selectedText = selectElement.options[selectElement.selectedIndex].text;

            // Limpa as opções existentes antes de adicionar novas
            selectElement.innerHTML = '';
            const option = document.createElement('option');
            option.value = '';
            option.text = 'Selecione uma afiliada';
            selectElement.appendChild(option);
            // Acessa o array "afiliadas" dentro da resposta JSON
            data.afiliadas.forEach(afiliada => {
              const option = document.createElement('option');
              option.value = afiliada.id;
              option.text = afiliada.nome;
              selectElement.appendChild(option);
            });
            selectElement.value = selectedValue;
            selectElement.options[selectElement.selectedIndex].text = selectedText;
  
          })
          .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
          });
    }
    document.getElementById('id_localidade').addEventListener('change', function() {
      fetchAfiliada();
    });
  });