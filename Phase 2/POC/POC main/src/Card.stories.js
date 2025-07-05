import CardDocumentation from './Card.mdx';

export default {
  title: 'Components/Card',
  parameters: {
    docs: {
      page: CardDocumentation, // Use MDX for documentation [10]
    },
  },
  argTypes: {
    title: { control: 'text' },
    description: { control: 'text' },
    imageUrl: { control: 'text' },
    state: { control: 'select', options: ['default', 'highlighted'] },
  },
};

const Template = ({ title, description, imageUrl, state }) => {
  const stateAttr = state === 'highlighted'? `data-state="highlighted"` : '';

  return `
    <div class="l-center" style="--mcss-l-center-max-width: 40ch;">
      <article
        class="c-card"
        ${stateAttr}
        vocab="http://www.mcss.dev/ns/v1# http://schema.org/"
        typeof="mcs:Component schema:Article"
        resource="#card-1"
      >
        <div property="mcs:purpose" content="A summary card for an article." class="u-visually-hidden"></div>
        <img class="c-card__image" src="${imageUrl}" alt="" rel="mcs:hasPart" property="schema:image" />
        <div class="c-card__content" rel="mcs:hasPart">
          <h3 class="c-card__title" property="schema:headline">${title}</h3>
          <p class="c-card__description" property="schema:description">${description}</p>
          <a href="#" class="c-button c-button--primary" property="mcs:interaction-type" content="click" rel="mcs:hasPart">
            <span property="mcs:consequence" content="Navigates to the full article." class="u-visually-hidden"></span>
            Read More
          </a>
        </div>
      </article>
    </div>
  `;
};

export const Default = Template.bind({});
Default.args = {
  title: 'The Future of CSS',
  description: 'Exploring how structured methodologies like MCSS are shaping AI-driven development.',
  imageUrl: 'https://via.placeholder.com/600x400',
  state: 'default',
};

export const Highlighted = Template.bind({});
Highlighted.args = {
 ...Default.args,
  state: 'highlighted',
};
