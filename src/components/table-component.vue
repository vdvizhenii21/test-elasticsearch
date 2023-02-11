<template>
  <div>
    <input type="text" v-model="searchTerm" @input="search"/>
    <table>
      <thead>
        <tr>
          <th v-for="column in columns" @click="sort(column)" :key="column.field">
            {{ column.label }}
            <span v-if="sortColumn === column && sortDirection === 'asc'" class="oi oi-caret-top"></span>
            <span v-if="sortColumn === column && sortDirection === 'desc'" class="oi oi-caret-bottom"></span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in filteredData" :key="row.id">
          <td v-for="column in columns" v-html="row[column.field]" :key="column.field"></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: [],
      columns: [],
      searchTerm: '',
      sortColumn: '',
      sortDirection: 'asc'
    };
  },
  mounted() {
    axios
      .get('http://localhost:9200/my-index/_search')
      .then(response => {
        this.data = response.data.hits.hits.map(hit => hit._source);
        this.columns = Object.keys(this.data[0]);
      });
  },
  computed: {
    filteredData() {
      return this.data
        .filter(row =>
          Object.values(row)
            .join('')
            .toLowerCase()
            .includes(this.searchTerm.toLowerCase())
        )
        .sort((a, b) => {
          if (this.sortColumn) {
            if (this.sortDirection === 'asc') {
              return a[this.sortColumn] > b[this.sortColumn]
                ? 1
                : -1;
            } else {
              return a[this.sortColumn] < b[this.sortColumn]
                ? 1
                : -1;
            }
          }
          return 0;
        });
    }
  },
  methods: {
    search() {
      // Update the filteredData computed property when the search term changes
    },
    sort(column) {
      if (this.sortColumn === column) {
        this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
        } else {
        this.sortColumn = column;
        this.sortDirection = 'asc';
      }
    }
  }
};
</script>