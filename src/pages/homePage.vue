<template>
  <div>
    <el-input placeholder="Type in whole sentences to search for papers." v-model="userInput">
      <template #append>
        <el-button type="primary" :icon="Search">search</el-button>
      </template>
    </el-input>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import {Search} from '@element-plus/icons-vue'
const userInput = ref('')
</script>

<style scoped>

</style>
