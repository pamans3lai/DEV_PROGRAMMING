import type { Speaker } from "./data";

const typeSpeakers = <T extends Record<string, Speaker>>(data: T): Record<keyof T, Speaker> =>
    Object.freeze(data);

export const speakers = typeSpeakers({
    'ihsan-muchtar': {
        name: 'Ihsan Muchtar',
        slug: 'ihsan-muchtar',
        handle: '@ihsanm',
        handleUrl: 'https://x.com/ihsan',
        picture: 'https://s.com',
        biography: 'f;alksdjf;lkas'
        
    }
});