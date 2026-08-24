// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	site: 'https://docs.stackblaze.com',
	redirects: {
		'/databases/overview': '/databases',
		'/docs': '/',
		'/docs/[...slug]': '/[...slug]',
	},
	integrations: [
		starlight({
			title: 'StackBlaze Docs',
			description:
				'Deploy apps, managed add-ons, and jobs on StackBlaze without running a cluster.',
			favicon: '/favicon.svg',
			logo: {
				src: './src/assets/logo.svg',
				alt: 'StackBlaze',
			},
			customCss: ['./src/styles/custom.css'],
			editLink: {
				baseUrl: 'https://github.com/stackblaze/docs/edit/main/',
			},
			components: {
				SiteTitle: './src/components/SiteTitle.astro',
				SocialIcons: './src/components/SocialIcons.astro',
			},
			sidebar: [
				{ slug: 'quickstart' },
				{ slug: 'concepts' },
				{ slug: 'agents' },
				{ slug: 'guides' },
				{ slug: 'blueprint' },
				{
					label: 'Platform',
					collapsed: true,
					items: [
						{ slug: 'platform', label: 'Overview' },
						{ slug: 'platform/migrate-from-heroku' },
						{
							label: 'Compare to StackBlaze',
							items: [
								{ label: 'Compare to Heroku', link: 'https://stackblaze.com/compare/heroku' },
								{ label: 'Compare to Render', link: 'https://stackblaze.com/compare/render' },
								{ label: 'Compare to Fly.io', link: 'https://stackblaze.com/compare/fly-io' },
								{ label: 'Compare to Railway', link: 'https://stackblaze.com/compare/railway' },
								{ label: 'Compare to Vercel', link: 'https://stackblaze.com/compare/vercel' },
							],
						},
					],
				},
				{
					label: 'Build & deploy',
					collapsed: true,
					items: [
						{ slug: 'build-deploy', label: 'Overview' },
						{ slug: 'build-deploy/apps' },
						{ slug: 'deploy/web-services' },
						{ slug: 'deploy/background-workers' },
						{ slug: 'deploy/cron-jobs' },
						{ slug: 'deploy/static-sites' },
						{ slug: 'deploy/github' },
						{ slug: 'deploy/docker' },
						{ slug: 'deploy/docker-compose' },
						{
							label: 'CI/CD',
							items: [
								{ slug: 'cicd/auto-deploy' },
								{ slug: 'cicd/pr-previews' },
								{ slug: 'cicd/deploy-hooks' },
								{ slug: 'cicd/rollbacks' },
								{ slug: 'cicd/monorepo' },
							],
						},
						{
							label: 'Scaling',
							items: [
								{ slug: 'scaling/horizontal' },
								{ slug: 'scaling/autoscaling' },
								{ slug: 'scaling/limits' },
								{ slug: 'scaling/zero-downtime' },
								{ slug: 'storage/health-checks' },
							],
						},
					],
				},
				{
					label: 'Data & storage',
					collapsed: true,
					items: [
						{ slug: 'data-storage', label: 'Overview' },
						{
							label: 'Databases',
							items: [
								{ slug: 'databases', label: 'Overview' },
								{ slug: 'databases/postgresql' },
								{ slug: 'databases/mysql' },
								{ slug: 'databases/redis' },
								{ slug: 'databases/mongodb' },
								{ slug: 'databases/cockroachdb' },
								{ slug: 'databases/clickhouse' },
								{ slug: 'databases/opensearch' },
								{ slug: 'databases/milvus' },
								{ slug: 'databases/cassandra' },
								{ slug: 'databases/scylladb' },
								{ slug: 'databases/couchdb' },
								{ slug: 'databases/memcached' },
								{ slug: 'databases/backups' },
								{ slug: 'databases/pitr' },
							],
						},
						{
							label: 'Volumes',
							items: [{ slug: 'storage/persistent-disks' }],
						},
						{
							label: 'Messaging',
							items: [{ slug: 'messaging/kafka' }, { slug: 'messaging/rabbitmq' }],
						},
					],
				},
				{
					label: 'Networking',
					collapsed: true,
					items: [
						{ slug: 'networking', label: 'Overview' },
						{ slug: 'networking/custom-domains' },
						{ slug: 'networking/ssl' },
						{ slug: 'networking/private-networking' },
						{ slug: 'networking/websockets' },
						{ slug: 'networking/redirects' },
					],
				},
				{
					label: 'Observability',
					collapsed: true,
					items: [
						{ slug: 'observability', label: 'Overview' },
						{ slug: 'operations/observability', label: 'Metrics, logs, and traces' },
						{ slug: 'operations/troubleshooting' },
					],
				},
				{
					label: 'Access',
					collapsed: true,
					items: [
						{ slug: 'access', label: 'Overview' },
						{ slug: 'security/env-vars' },
						{ slug: 'security/secret-files' },
						{ slug: 'security/team-permissions' },
						{ slug: 'security/two-factor-auth' },
						{ slug: 'security/ip-allowlist' },
					],
				},
				{
					label: 'Reference',
					collapsed: true,
					items: [
						{ slug: 'reference', label: 'Overview' },
						{ slug: 'reference/api' },
						{ slug: 'reference/cli', label: 'Automation' },
						{ slug: 'reference/limits' },
						{ slug: 'reference/pricing' },
					],
				},
			],
		}),
	],
});
