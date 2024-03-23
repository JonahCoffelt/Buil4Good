<template>
  <header>
    <div class="logo">Your Logo Here</div>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'WebsiteHeader',
  // You can add data, methods, computed properties here if needed
};
</script>

<style>
header {
  background-color: #333;
  color: white;
  padding: 1rem;
}

.logo {
  font-size: 1.5rem;
}

nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline-block;
  margin-right: 1rem;
}

nav ul li a {
  color: white;
  text-decoration: none;
}

</style>
