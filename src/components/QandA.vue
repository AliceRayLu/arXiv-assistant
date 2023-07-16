<template>
  <el-row style="margin-top: 2vh">
    <el-avatar :icon="UserFilled" size="large" />
    <el-card style="margin-left: 0.5vw">
      <div>{{ props.question }}</div>
    </el-card>
  </el-row>
  <el-row v-if="props.isSend" style="margin-top: 2vh">
    <el-avatar size="large">Agent</el-avatar>
    <el-card style="margin-left: 0.5vw">
      <div>hahahah</div>
    </el-card>
  </el-row>
</template>

<script lang="ts" setup>
import { UserFilled } from "@element-plus/icons-vue";
const props = defineProps({
  question: String,
  isSend: Boolean,
});
</script>
