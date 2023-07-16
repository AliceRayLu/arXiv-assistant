<template>
  <el-row class="role">
    <el-avatar :icon="UserFilled" size="large" />
    <el-card style="margin-left: 0.5vw">
      <div>{{ props.question }}</div>
    </el-card>
  </el-row>
  <el-row class="role">
    <el-avatar size="large">Agent</el-avatar>
    <el-card style="margin-left: 0.5vw">
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

<style>
.role {
  margin-top: 2vh;
  margin-bottom: 2vh;
}
</style>
