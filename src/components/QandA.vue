<template>
  <el-row>
    <el-avatar :icon="UserFilled" />
    <el-card style="margin-left: 0.5vw">
      <div>lalalala</div>
    </el-card>
  </el-row>
</template>

<script lang="ts" setup>
import { UserFilled } from "@element-plus/icons-vue";
const props = defineProps({
  question: String,
});
</script>
