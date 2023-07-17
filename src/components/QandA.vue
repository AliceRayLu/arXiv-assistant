<template>
  <el-row class="role" style="display: flex; justify-content: flex-end">
    <el-card
      class="card"
      shadow="never"
      :body-style="{
        backgroundColor: 'rgba(0,0,0,.05)',
        borderRadius: '1vh',
        border: '0px solid ',
      }"
    >
      <div>{{ props.question }}</div>
    </el-card>
    <el-avatar :icon="UserFilled" size="large" />
  </el-row>
  <el-row class="role">
    <el-avatar size="large">Agent</el-avatar>
    <el-card
      class="card"
      shadow="never"
      :body-style="{
        backgroundColor: 'rgba(98,106,239,.1)',
        borderRadius: '1vh',
        border: '0px',
      }"
    >
      <div>{{ answer }}</div>
    </el-card>
  </el-row>
</template>

<script lang="ts" setup>
import { UserFilled } from "@element-plus/icons-vue";
const props = defineProps({
  question: String,
  answer: String,
});
</script>

<style scoped>
.role {
  margin-top: 2vh;
  margin-bottom: 2vh;
}
.card {
  margin-left: 0.5vw;
  margin-right: 0.5vw;
}
/deep/.el-card {
  border: none;
}
</style>
