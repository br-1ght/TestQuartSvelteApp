<script>
    let errors = ""
    const logoutSubmit = async () => {
        const response = await fetch("http://localhost:5000/api/user/logout", {
            method: "POST",
            credentials: "include",
            headers: {
                "Accept": "application/json"
            }
        })
        const result = await response.json() 

        if (!response.ok) {
            errors = result
        }
    }
</script>

<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">TestQuartApp</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon">▼</span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" href="/users">Users</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/message">Message</a>
        </li>
        <li class="nav-item">
            <form action="" on:submit={logoutSubmit}>
                <button type="submit" class="btn nav-link">Logout</button>
            </form>
        </li>
      </ul>
      
      <div class="d-flex">
        <a href="/login" class="nav-link">Login</a>
      </div>
    </div>
  </div>
</nav>