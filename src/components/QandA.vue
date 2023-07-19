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
        maxWidth: '70vw',
      }"
    >
      <div>{{ props.answer.answer }}</div>
      <div style="margin-top: 3vh">
        The answer is generated according to the following papers.
      </div>
      <div
        v-for="info in props.answer.papers"
        v-bind:key="info"
        style="margin-top: 3vh"
      >
        <!--        <el-form label-width="10vw" size="large" :inline="true">-->
        <!--          <el-form-item label="Title">{{ info.title }}</el-form-item>-->
        <!--        </el-form>-->
        <div>title:{{ info.title }}</div>
        <div v-if="info.author !== null">author:{{ info.author }}</div>
        <div v-else>author: unknown</div>
        <div v-if="info.detail !== 'unknown'">
          Visit <a ref="{{info.detail}}">{{ info.detail }}</a> to see
          details.<br />
          Visit <a ref="{{info.pdf}}">{{ info.pdf }}</a> to see the paper.
        </div>
        <div v-else>404-Can't find the paper's source page</div>
        <div>categories:{{ info.categories }}</div>
      </div>
    </el-card>
  </el-row>
</template>

<script lang="ts" setup>
import { UserFilled } from "@element-plus/icons-vue";
import { AIAnswer } from "@/utils/paperInfo";
const props = defineProps<{
  question: string;
  answer: AIAnswer;
}>();
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
