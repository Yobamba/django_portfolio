
// Function to get values from the dom for filtering purposes
function getSelectedFilters() {
    const language = document.getElementById('languages').value;
    const framework = document.getElementById('frameworks').value;
    const projectType = document.getElementById('projectType').value;

    
    filterProjects(language, framework, projectType);
}

// Function to filter through projects
function filterProjects(language, framework, projectType) {
    

    const projects = document.querySelectorAll('.proj');

    projects.forEach(project => {
        const languageMatch = project.classList.contains(language);
        const frameworkMatch = project.classList.contains(framework);
        const projectTypeMatch = project.classList.contains(projectType);

        if (languageMatch || frameworkMatch || projectTypeMatch) {
            project.style.display = 'contents'; // Show project
        } else {
            project.style.display = 'none'; // Hide project
        }
    });
}

    


// Event listeners for filter options
document.getElementById('languages').addEventListener('change', getSelectedFilters);
document.getElementById('frameworks').addEventListener('change', getSelectedFilters);
document.getElementById('projectType').addEventListener('change', getSelectedFilters);




// // Function to filter projects based on user selection
// function filterProjects(language, framework, projectType) {
//     const language = document.querySelector('.languages').value;
//     const framework = document.querySelector('.frameworks').value;
//     const projectType = document.querySelector('.projectType').value;

//     const projects = document.querySelectorAll('.proj');

//     projects.forEach(project => {
//         const languageMatch = project.textContent.includes(language);
//         const frameworkMatch = project.textContent.includes(framework);
//         const projectTypeMatch = project.textContent.includes(projectType);

//         if (languageMatch && frameworkMatch && projectTypeMatch) {
//             project.style.display = 'block'; // Show project
//         } else {
//             project.style.display = 'none'; // Hide project
//         }
//     });
// }

// // Event listeners for filter options
// document.getElementById('languages').addEventListener('change', filterProjects);
// document.getElementById('frameworks').addEventListener('change', filterProjects);
// document.getElementById('projectType').addEventListener('change', filterProjects);

// // Initial filter when page loads
// filterProjects();

// fetch('/projects/')
//   .then(response => response.json())
//   .then(data => {
//     const projectsContainer = document.getElementById('projects-container');
//     data.forEach(project => {
//       const projectDiv = document.createElement('div');
//       projectDiv.classList.add('proj');

//       const projectTitle = document.createElement('h2');
//       const projectLink = document.createElement('a');
//       projectLink.href = project.image_url;
//       projectLink.textContent = project.name;
//       projectTitle.appendChild(projectLink);

//       const projectDescription = document.createElement('p');
//       projectDescription.textContent = project.description;

//       projectDiv.appendChild(projectTitle);
//       projectDiv.appendChild(projectDescription);

//       projectsContainer.appendChild(projectDiv);
//     });
//   })
//   .catch(error => console.error('Error fetching projects:', error));


