<template>
  <div>
    <h1>Notion Data</h1>
    <ul>
      <li v-for="item in data" :key="item.id">{{ item.properties.Name.title[0].plain_text }}</li>
      <li v-for="item in data" :key="item.id">{{ item.properties.Price.number }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: [],
    };
  },
  mounted() {
    axios.get('http://localhost:3000/fetchData')
      .then(response => {
        this.data = response.data;
        console.log(this.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  },
};
</script>