<template>
  <div v-if="notionPage">
    <vue-notion-render :blockMap="notionPage.block" />
  </div>
  <div v-else>
    Loading...
  </div>
</template>

<script>
import VueNotionRender from 'vue-notion-render';
import { NotionAPI } from 'notion-client';

export default {
  name: 'NotionPage',
  components: {
    VueNotionRender,
  },
  data() {
    return {
      notionPage: null,
    };
  },
  async created() {
    const notion = new NotionAPI();
    try {
      const pageId = 'YOUR_PAGE_ID_HERE';
      const response = await notion.getPage(pageId);
      this.notionPage = response;
    } catch (error) {
      console.error('Error fetching Notion page:', error);
    }
  },
};
</script>